
import { useState, useCallback } from 'react';
import { GoogleGenAI, GenerateContentResponse, Type } from '@google/genai';
import type { AnalysisResult, FinancialMetric, CompetitiveAnalysis, StockRecommendation, Forecast, RiskAssessment } from '../types';

const API_KEY = process.env.API_KEY;
if (!API_KEY) {
  throw new Error("API_KEY environment variable not set.");
}

const ai = new GoogleGenAI({ apiKey: API_KEY, vertexai: true });

const fileToGenerativePart = async (file: File) => {
  const base64EncodedData = await new Promise<string>((resolve) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve((reader.result as string).split(',')[1]);
    reader.readAsDataURL(file);
  });
  return {
    inlineData: {
      data: base64EncodedData,
      mimeType: file.type,
    },
  };
};

const parseJsonResponse = <T>(text: string, step: string): T => {
    try {
        // The model sometimes returns JSON wrapped in markdown ```json ... ```
        const cleanText = text.replace(/^```json\s*|```$/g, '').trim();
        return JSON.parse(cleanText) as T;
    } catch (e) {
        console.error(`Failed to parse JSON for step: ${step}`, { text });
        throw new Error(`The model returned an invalid format for ${step}. Please try again.`);
    }
};

// FIX: Add robust API call handler with exponential backoff
const generateContentWithRetry = async (
  params: any, // Using 'any' as GenerateContentRequest is not an exported type
  maxRetries = 3,
  initialDelay = 1000
): Promise<GenerateContentResponse> => {
  let retries = 0;
  let delay = initialDelay;
  while (true) {
    try {
      const response = await ai.models.generateContent(params);
      
      if (!response.text && (!response.candidates || response.candidates.length === 0)) {
          throw new Error("API returned an empty or invalid response.");
      }
      
      return response;
    } catch (error: any) {
      retries++;
      if (retries >= maxRetries) {
        console.error("API call failed after multiple retries", { params, error });
        if (error.message.includes('429')) {
             throw new Error("API rate limit exceeded. Please wait and try again later.");
        }
        if (error.message.includes('500') || error.message.includes('503') || error.message.includes('504')) {
            throw new Error("The analysis service is temporarily unavailable (server error). Please try again later.");
        }
        throw new Error(`An API error occurred during analysis: ${error.message}`);
      }
      console.warn(`API call failed, retrying in ${delay}ms... (Attempt ${retries}/${maxRetries})`, error.message);
      await new Promise(resolve => setTimeout(resolve, delay));
      delay *= 2; // Exponential backoff
    }
  }
};

export const useFinancialAnalysis = () => {
  const [progress, setProgress] = useState('');

  const analyze = useCallback(async (file: File): Promise<AnalysisResult> => {
    if (!file) throw new Error('No file provided for analysis.');

    const pdfPart = await fileToGenerativePart(file);

    // Step 1: Extract Financial Metrics
    setProgress('Step 1/6: Extracting financial metrics...');
    const metricsResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [pdfPart, { text: "Analyze this earnings report. Extract the company name, ticker symbol, reporting period (e.g., Q2 2024), and key financial metrics. For each metric, provide the value, Year-over-Year (YoY) change, and Quarter-over-Quarter (QoQ) change. If a change is not available, state 'N/A'." }] },
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
                type: Type.OBJECT,
                properties: {
                    companyName: { type: Type.STRING },
                    tickerSymbol: { type: Type.STRING },
                    period: { type: Type.STRING },
                    financials: {
                        type: Type.ARRAY,
                        items: {
                            type: Type.OBJECT,
                            properties: {
                                name: { type: Type.STRING },
                                value: { type: Type.STRING },
                                yoyChange: { type: Type.STRING },
                                qoqChange: { type: Type.STRING },
                            },
                            required: ['name', 'value', 'yoyChange', 'qoqChange']
                        }
                    }
                },
                required: ['companyName', 'tickerSymbol', 'period', 'financials']
            }
        }
    });
    const metricsData = parseJsonResponse<{ companyName: string; tickerSymbol: string; period: string; financials: FinancialMetric[] }>(metricsResponse.text, 'Financial Metrics');

    // Step 2: Generate Executive Summary
    setProgress('Step 2/6: Generating executive summary...');
    const summaryResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [{ text: `Based on the following financial data for ${metricsData.companyName} (${metricsData.tickerSymbol}) for ${metricsData.period}, write a concise, professional executive summary of the company's performance. Data: ${JSON.stringify(metricsData.financials)}` }] },
    });
    const executiveSummary = summaryResponse.text;

    // Step 3: Competitive Analysis
    setProgress('Step 3/6: Gathering competitive intelligence...');
    const competitionResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [{ text: `Provide a competitive analysis for ${metricsData.companyName}. Identify 2-3 main competitors and briefly describe their recent performance or market position. Use web search to get current data.` }] },
        config: { tools: [{ googleSearch: {} }] }
    });
    const competitionText = competitionResponse.text;
    const competitionSources = competitionResponse.candidates?.[0]?.groundingMetadata?.groundingChunks?.map(chunk => chunk.web) ?? [];
    const competition: CompetitiveAnalysis = {
        summary: competitionText,
        competitors: [], // Model provides this in the summary text
        sources: competitionSources.filter(source => source?.uri).map(source => ({ title: source.title || 'Source', uri: source.uri! }))
    };

    // Step 4: Stock Recommendation
    setProgress('Step 4/6: Generating stock recommendation...');
    const recommendationResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [{ text: `Act as a professional equity research analyst. Given the financial data: ${JSON.stringify(metricsData.financials)} and competitive landscape: "${competition.summary}", provide a stock recommendation for ${metricsData.tickerSymbol}.` }] },
        config: {
            systemInstruction: "Your analysis must be balanced. Support all claims with evidence from the provided data. Conclude with a clear BUY, HOLD, or SELL rating. Never guarantee returns.",
            responseMimeType: 'application/json',
            responseSchema: {
                type: Type.OBJECT,
                properties: {
                    recommendation: { type: Type.STRING, enum: ['BUY', 'HOLD', 'SELL'] },
                    rationale: { type: Type.STRING },
                    bullishPoints: { type: Type.ARRAY, items: { type: Type.STRING } },
                    bearishPoints: { type: Type.ARRAY, items: { type: Type.STRING } },
                },
                required: ['recommendation', 'rationale', 'bullishPoints', 'bearishPoints']
            }
        }
    });
    const recommendation = parseJsonResponse<StockRecommendation>(recommendationResponse.text, 'Stock Recommendation');

    // Step 5: Earnings Forecasting
    setProgress('Step 5/6: Creating earnings forecast...');
    const forecastResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [{ text: `Based on the provided earnings data and trends for ${metricsData.companyName}, create a financial forecast. Data: ${JSON.stringify(metricsData.financials)}` }] },
        config: {
            systemInstruction: "Provide a forecast for next quarter's revenue and EPS, and a 12-month stock price target. Crucially, you must state the key assumptions underpinning your forecast.",
            responseMimeType: 'application/json',
            responseSchema: {
                type: Type.OBJECT,
                properties: {
                    nextQuarter: {
                        type: Type.OBJECT,
                        properties: {
                            revenue: { type: Type.STRING },
                            eps: { type: Type.STRING },
                        },
                        required: ['revenue', 'eps']
                    },
                    priceTarget12Month: { type: Type.STRING },
                    assumptions: { type: Type.ARRAY, items: { type: Type.STRING } },
                },
                required: ['nextQuarter', 'priceTarget12Month', 'assumptions']
            }
        }
    });
    const forecast = parseJsonResponse<Forecast>(forecastResponse.text, 'Earnings Forecast');

    // Step 6: Risk Assessment
    setProgress('Step 6/6: Assessing risks and catalysts...');
    const riskResponse = await generateContentWithRetry({
        model: 'gemini-2.5-flash',
        contents: { role: 'user', parts: [{ text: `Identify the primary risks (headwinds) and potential catalysts (tailwinds) for ${metricsData.companyName} over the next 12 months, considering its recent performance and the competitive environment. Data: ${JSON.stringify(metricsData.financials)}, Competition: "${competition.summary}"` }] },
        config: {
            systemInstruction: "Provide a balanced assessment. For each risk, suggest a potential mitigation. For each catalyst, describe its potential impact.",
            responseMimeType: 'application/json',
            responseSchema: {
                type: Type.OBJECT,
                properties: {
                    risks: {
                        type: Type.ARRAY,
                        items: {
                            type: Type.OBJECT,
                            properties: {
                                risk: { type: Type.STRING },
                                mitigation: { type: Type.STRING },
                            },
                            required: ['risk', 'mitigation']
                        }
                    },
                    catalysts: {
                        type: Type.ARRAY,
                        items: {
                            type: Type.OBJECT,
                            properties: {
                                catalyst: { type: Type.STRING },
                                impact: { type: Type.STRING },
                            },
                            required: ['catalyst', 'impact']
                        }
                    },
                },
                required: ['risks', 'catalysts']
            }
        }
    });
    const risks = parseJsonResponse<RiskAssessment>(riskResponse.text, 'Risk Assessment');

    setProgress('Analysis complete.');

    return {
      ...metricsData,
      executiveSummary,
      competition,
      recommendation,
      forecast,
      risks,
    };
  }, []);

  return { analyze, progress };
};
