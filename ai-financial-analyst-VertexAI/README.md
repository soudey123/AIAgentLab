# 🤖 AI Financial Analyst

**Powered by Google Gemini & Vertex AI**

An intelligent financial analysis application that transforms corporate earnings reports (PDFs) into comprehensive investment insights. Built with React, TypeScript, and Google's Gemini 2.5 Flash model, this application provides institutional-grade financial analysis in minutes.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Integration](#api-integration)
- [Analysis Pipeline](#analysis-pipeline)
- [Components](#components)
- [Types & Interfaces](#types--interfaces)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

---

## 🎯 Overview

The AI Financial Analyst is a sophisticated web application that leverages Google's Gemini AI to analyze corporate earnings reports and deliver actionable investment insights. Users simply upload a PDF earnings report, and the application:

1. **Extracts** key financial metrics (revenue, margins, cash flow, ratios)
2. **Analyzes** competitive positioning using real-time web search
3. **Generates** BUY/HOLD/SELL stock recommendations with detailed rationale
4. **Forecasts** next quarter earnings and 12-month price targets
5. **Assesses** risks (headwinds) and catalysts (tailwinds)
6. **Presents** everything in a professional, interactive dashboard

---

## ✨ Features

### 🔍 **Multi-Step AI Analysis Pipeline**
- **6-stage sequential analysis** for comprehensive insights
- Real-time progress tracking with user feedback
- Exponential backoff retry logic for API resilience

### 📊 **Financial Metrics Extraction**
- Automatic identification of company name, ticker symbol, and reporting period
- Key metrics: Revenue, EPS, Operating Margin, Free Cash Flow, ROE, ROA
- Year-over-Year (YoY) and Quarter-over-Quarter (QoQ) growth calculations

### 🌐 **Competitive Intelligence**
- Web search integration via Google Search grounding
- Benchmarking against 2-3 primary competitors
- Citation of sources for competitive data

### 📈 **Stock Recommendation Engine**
- Clear BUY/HOLD/SELL rating with confidence justification
- Bullish and bearish points analysis
- Evidence-based rationale tied to financial performance

### 🔮 **Earnings & Price Forecasting**
- Next quarter revenue and EPS estimates
- 12-month stock price target
- Key assumptions underpinning all forecasts

### ⚠️ **Risk Assessment**
- Identification of primary risks with mitigation strategies
- Positive catalysts with potential impact analysis
- Balanced view of opportunities and threats

### 🎨 **Modern UI/UX**
- Responsive design built with Tailwind CSS
- Drag-and-drop file upload with visual feedback
- Interactive dashboard with collapsible sections
- Clean, professional presentation suitable for investors

---

## 🏗️ Architecture

This application follows a **modular, component-based architecture** with clear separation of concerns:

```
┌─────────────────────────────────────────────────────┐
│                   User Interface                     │
│              (React + TypeScript + Tailwind)         │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│              State Management Layer                  │
│         (React Hooks: useState, useCallback)         │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│           Custom Hook: useFinancialAnalysis          │
│        (Orchestrates 6-step analysis pipeline)       │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│             Google Gemini API Client                 │
│         (@google/genai via Vertex AI)                │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│               Gemini 2.5 Flash Model                 │
│    (Financial Analysis + Web Search Grounding)       │
└─────────────────────────────────────────────────────┘
```

### **Key Design Patterns:**
- **Container/Presentational Components**: Logic separated from UI
- **Custom Hook Pattern**: Encapsulated API logic in `useFinancialAnalysis`
- **Structured Output via JSON Schema**: Enforces consistent, parseable responses
- **Progressive Enhancement**: Multi-step pipeline with user feedback
- **Retry with Exponential Backoff**: Resilient API error handling

---

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| **Frontend Framework** | React 18.3.1 |
| **Language** | TypeScript |
| **Styling** | Tailwind CSS (CDN) |
| **AI/LLM** | Google Gemini 2.5 Flash via Vertex AI |
| **API Client** | `@google/genai` (official Google SDK) |
| **Build Tool** | Native ES Modules (importmap) |
| **Module Loading** | ESM.sh (CDN for npm packages) |
| **Runtime** | Browser (client-side rendering) |

---

## 📦 Installation

### **Prerequisites**
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Google Cloud Platform account with Vertex AI enabled
- API key for Gemini via Vertex AI

### **Setup Steps**

1. **Clone or download the project**
```bash
# If using version control
git clone <repository-url>
cd ai-financial-analyst

# Or simply extract the ZIP file
unzip ai-financial-analyst.zip
cd ai-financial-analyst
```

2. **No build step required!** This application uses ES modules via CDN, so there's no compilation needed.

3. **Configure environment variables** (see [Configuration](#configuration) section)

4. **Serve the application**
```bash
# Using Python's built-in server
python -m http.server 8000

# Or using Node.js http-server
npx http-server -p 8000

# Or any static file server of your choice
```

5. **Open in browser**
```
http://localhost:8000
```

---

## ⚙️ Configuration

### **Environment Variables**

The application requires a **Vertex AI API key** to function. Set this in your environment:

**Option 1: Environment variable (recommended for deployment)**
```bash
export API_KEY="your-vertex-ai-api-key"
```

**Option 2: Modify code directly (development only)**

Edit `hooks/useFinancialAnalysis.ts`:
```typescript
const API_KEY = 'your-vertex-ai-api-key'; // Line 6
```

⚠️ **Security Warning**: Never commit API keys to version control. Use environment variables or secret management services in production.

### **Getting a Vertex AI API Key**

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the **Vertex AI API**
3. Navigate to **APIs & Services > Credentials**
4. Create a new API key or use an existing one
5. Ensure your project has Vertex AI enabled and proper billing configured

### **Model Configuration**

The application uses **Gemini 2.5 Flash** by default. To change models, edit `hooks/useFinancialAnalysis.ts`:

```typescript
model: 'gemini-2.5-flash', // Change to 'gemini-2.5-pro' for higher quality
```

Available models:
- `gemini-2.5-flash` - Fast, cost-effective (recommended)
- `gemini-2.5-pro` - Higher quality, slower, more expensive
- `gemini-1.5-flash` - Previous generation
- `gemini-1.5-pro` - Previous generation, higher quality

---

## 🚀 Usage

### **Step-by-Step Guide**

1. **Open the application** in your web browser
2. **Upload an earnings report PDF**
   - Click the upload area or drag-and-drop a PDF file
   - Supported format: PDF only
   - Recommended: Corporate quarterly/annual earnings reports
3. **Wait for analysis** (typically 45-90 seconds)
   - Progress indicator shows current step (1/6 through 6/6)
4. **Review the dashboard**
   - Executive Summary
   - Financial Highlights Table
   - Competitive Positioning
   - Stock Recommendation (BUY/HOLD/SELL)
   - Earnings Forecast & Price Target
   - Risk Assessment (Risks & Catalysts)
5. **Start a new analysis** by clicking "Analyze Another Report"

### **Example Use Cases**

- **Equity Research Analysts**: Automate initial earnings report analysis
- **Portfolio Managers**: Quick competitive intelligence and recommendation
- **Individual Investors**: Understand company performance before investing
- **Students/Educators**: Learn financial analysis frameworks
- **Corporate Finance Teams**: Competitive benchmarking

---

## 📁 Project Structure

```
ai-financial-analyst/
├── index.html                          # Entry point HTML file
├── index.tsx                           # React root rendering
├── App.tsx                             # Main application component
├── metadata.json                       # Project metadata
├── types.ts                            # TypeScript interfaces
├── components/
│   ├── Header.tsx                      # Application header
│   ├── FileUpload.tsx                  # PDF upload interface
│   ├── AnalysisProgress.tsx            # Progress indicator
│   ├── AnalysisDashboard.tsx           # Results dashboard
│   ├── ErrorDisplay.tsx                # Error handling UI
│   └── icons.tsx                       # SVG icon components
├── hooks/
│   └── useFinancialAnalysis.ts         # Core AI analysis logic
└── README.md                           # This file
```

### **File Descriptions**

| File | Purpose |
|------|---------|
| `index.html` | Loads Tailwind CSS, React, and sets up ES module imports |
| `index.tsx` | Renders the root React component |
| `App.tsx` | Main application logic, state management, and routing |
| `types.ts` | TypeScript type definitions for all data structures |
| `useFinancialAnalysis.ts` | Custom hook containing the 6-step AI analysis pipeline |
| Component files | Reusable UI components for different app states |

---

## 🔌 API Integration

### **Google Gemini API Client**

The application uses the official `@google/genai` SDK:

```typescript
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({ 
  apiKey: API_KEY, 
  vertexai: true 
});
```

### **API Call Pattern**

Each analysis step follows this pattern:

```typescript
const response = await generateContentWithRetry({
  model: 'gemini-2.5-flash',
  contents: { 
    role: 'user', 
    parts: [pdfPart, { text: 'Your prompt here' }] 
  },
  config: {
    responseMimeType: 'application/json',
    responseSchema: { /* Your schema */ }
  }
});
```

### **Retry Logic**

The application implements exponential backoff for resilience:

```typescript
const generateContentWithRetry = async (
  params: any,
  maxRetries = 3,
  initialDelay = 1000
): Promise<GenerateContentResponse> => {
  // Retries up to 3 times with exponential backoff
  // Handles 429 (rate limit), 500, 503, 504 errors
}
```

### **Web Search Grounding**

Competitive analysis uses Google Search grounding:

```typescript
config: { 
  tools: [{ googleSearch: {} }] 
}
```

This allows the model to fetch real-time competitive data from the web.

---

## 🔄 Analysis Pipeline

The application performs **6 sequential analysis steps**, each calling the Gemini API:

### **Step 1: Financial Metrics Extraction**
- **Input**: PDF earnings report
- **Output**: Company name, ticker, period, financial metrics with YoY/QoQ changes
- **Schema**: Structured JSON with required fields
- **Model**: Gemini 2.5 Flash

### **Step 2: Executive Summary Generation**
- **Input**: Extracted financial data
- **Output**: 2-3 sentence professional summary of performance
- **Model**: Gemini 2.5 Flash

### **Step 3: Competitive Intelligence**
- **Input**: Company name
- **Output**: Analysis of 2-3 competitors with web-sourced data
- **Tools**: Google Search grounding enabled
- **Citations**: Web sources returned with `groundingMetadata`
- **Model**: Gemini 2.5 Flash

### **Step 4: Stock Recommendation**
- **Input**: Financial data + competitive landscape
- **Output**: BUY/HOLD/SELL rating with bullish/bearish points
- **System Instruction**: Enforce balanced analysis, evidence-based claims
- **Schema**: Structured JSON with enum for recommendation
- **Model**: Gemini 2.5 Flash

### **Step 5: Earnings Forecast**
- **Input**: Historical financial data and trends
- **Output**: Next quarter estimates (revenue, EPS), 12-month price target
- **System Instruction**: Require explicit assumptions
- **Schema**: Structured forecast with required fields
- **Model**: Gemini 2.5 Flash

### **Step 6: Risk Assessment**
- **Input**: Financial data + competitive context
- **Output**: List of risks with mitigations, catalysts with impacts
- **System Instruction**: Balanced assessment required
- **Schema**: Array of risk/catalyst objects
- **Model**: Gemini 2.5 Flash

---

## 🧩 Components

### **App.tsx**
Main application component managing global state and routing between views.

**State:**
- `analysisState`: 'idle' | 'analyzing' | 'success' | 'error'
- `analysisResult`: Complete analysis data
- `error`: Error message if analysis fails

**Key Methods:**
- `handleFileAnalysis()`: Initiates analysis pipeline
- `handleReset()`: Returns to upload screen

### **Header.tsx**
Static header displaying app title and branding.

### **FileUpload.tsx**
Drag-and-drop PDF upload interface.

**Props:**
- `onFileUpload: (file: File) => void`

**Features:**
- Drag-and-drop support
- Click-to-browse fallback
- PDF validation
- Visual feedback on hover/drop

### **AnalysisProgress.tsx**
Shows current analysis step with loading animation.

**Props:**
- `progress: string` - Current step description

### **AnalysisDashboard.tsx**
Main results display with 6 collapsible sections.

**Props:**
- `result: AnalysisResult` - Complete analysis data
- `onReset: () => void` - Callback to start over

**Sections:**
1. Executive Summary
2. Financial Highlights (table format)
3. Competitive Positioning (with source citations)
4. Stock Recommendation (with rating badge)
5. Earnings Forecast (estimates & price target)
6. Risk Assessment (risks & catalysts)

### **ErrorDisplay.tsx**
Error message display with retry option.

**Props:**
- `error: string | null` - Error message
- `onReset: () => void` - Callback to retry

### **icons.tsx**
SVG icon components (Upload, Chart, TrendingUp, AlertTriangle, etc.)

---

## 📐 Types & Interfaces

### **FinancialMetric**
```typescript
interface FinancialMetric {
  name: string;        // e.g., "Revenue"
  value: string;       // e.g., "$76.7B"
  yoyChange: string;   // e.g., "+11%"
  qoqChange: string;   // e.g., "+3%"
}
```

### **CompetitiveAnalysis**
```typescript
interface CompetitiveAnalysis {
  summary: string;                    // Text analysis
  competitors: {
    name: string;
    notes: string;
  }[];
  sources: {                          // Web sources
    title: string;
    uri: string;
  }[];
}
```

### **StockRecommendation**
```typescript
interface StockRecommendation {
  recommendation: 'BUY' | 'HOLD' | 'SELL';
  rationale: string;
  bullishPoints: string[];
  bearishPoints: string[];
}
```

### **Forecast**
```typescript
interface Forecast {
  nextQuarter: {
    revenue: string;
    eps: string;
  };
  priceTarget12Month: string;
  assumptions: string[];
}
```

### **RiskAssessment**
```typescript
interface RiskAssessment {
  risks: {
    risk: string;
    mitigation: string;
  }[];
  catalysts: {
    catalyst: string;
    impact: string;
  }[];
}
```

### **AnalysisResult**
```typescript
interface AnalysisResult {
  companyName: string;
  tickerSymbol: string;
  period: string;
  executiveSummary: string;
  financials: FinancialMetric[];
  competition: CompetitiveAnalysis;
  recommendation: StockRecommendation;
  forecast: Forecast;
  risks: RiskAssessment;
}
```

---

## 🛡️ Error Handling

The application implements robust error handling at multiple levels:

### **API-Level Errors**
- **429 Rate Limit**: "API rate limit exceeded. Please wait and try again."
- **500/503/504 Server Errors**: "Service temporarily unavailable. Please retry."
- **Network Errors**: Exponential backoff with 3 retry attempts

### **Data Parsing Errors**
- JSON parsing failures caught and reported per-step
- Markdown-wrapped JSON automatically cleaned (```json...```)
- Fallback error messages for invalid model responses

### **User-Facing Errors**
- Clear error messages displayed in UI
- "Try Again" button to restart analysis
- Error state preserved until user action

### **File Validation**
- PDF-only upload enforcement
- File size checks (implicit via browser)
- MIME type validation

---

## ⚠️ Limitations

### **Current Limitations**
1. **PDF-Only Input**: Does not support HTML, Word, or other document formats
2. **English Language**: Optimized for English-language earnings reports
3. **US Market Focus**: Assumes US GAAP accounting standards
4. **No Historical Data**: Analysis limited to single document, no time-series
5. **Rate Limits**: Subject to Vertex AI API quotas (varies by project)
6. **No User Authentication**: Single-session, no data persistence
7. **Client-Side Processing**: API key exposed in browser (use server-side proxy in production)

### **Known Issues**
- Large PDFs (>50 pages) may exceed context window limits
- Complex tables/charts may not extract perfectly
- Non-standard report formats may reduce accuracy
- Competitor identification may miss niche players

---

## 🚀 Future Enhancements

### **Short-Term (v2.0)**
- [ ] Support for multiple file formats (HTML, DOCX, TXT)
- [ ] Historical comparison across multiple quarters/years
- [ ] Export analysis as PDF report
- [ ] Save/load past analyses (local storage)
- [ ] Dark mode UI

### **Medium-Term (v3.0)**
- [ ] Server-side API proxy for secure key management
- [ ] User authentication and profile management
- [ ] Portfolio-level analysis (multiple companies)
- [ ] Customizable analysis templates
- [ ] Email/Slack notifications on completion

### **Long-Term (v4.0)**
- [ ] Real-time stock price integration
- [ ] Automated periodic re-analysis
- [ ] Natural language query interface ("How is Apple performing?")
- [ ] Integration with brokerage APIs for trade execution
- [ ] Multi-language support (Spanish, Mandarin, etc.)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### **Ways to Contribute**
1. **Report Bugs**: Open an issue with steps to reproduce
2. **Suggest Features**: Propose enhancements via issues
3. **Submit Pull Requests**: Fix bugs or add features
4. **Improve Documentation**: Clarify or expand this README
5. **Share Feedback**: How are you using the app? What's missing?

### **Development Workflow**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request with description

### **Code Style Guidelines**
- Follow existing TypeScript/React patterns
- Use meaningful variable and function names
- Add comments for complex logic
- Maintain type safety (no `any` types without justification)
- Keep components small and focused

---

## 📄 License

This project is provided as-is for educational and demonstrative purposes. 

**Usage Terms:**
- ✅ Free to use for personal projects
- ✅ Free to modify and extend
- ✅ Free to use as a learning resource
- ❌ Not licensed for commercial redistribution without permission
- ❌ No warranty or support guarantees

For commercial licensing inquiries, please contact the project maintainer.

---

## ⚖️ Disclaimer

**IMPORTANT LEGAL NOTICE**

This application is provided **for informational and educational purposes only**. It is **NOT** intended to provide:

- Financial advice
- Investment recommendations
- Professional analysis suitable for making trading decisions
- Regulatory-compliant equity research

**By using this application, you acknowledge that:**

1. **Not Financial Advice**: The analysis generated is produced by an AI model and should not be considered professional financial advice. Always consult a licensed financial advisor before making investment decisions.

2. **No Guarantees**: Past performance does not guarantee future results. AI-generated forecasts are speculative and may be inaccurate.

3. **User Responsibility**: You are solely responsible for any investment decisions you make. The creators of this application assume no liability for financial losses.

4. **Data Accuracy**: The application relies on AI interpretation of PDF documents and web-sourced data, which may contain errors, omissions, or outdated information.

5. **Not Regulatory Compliant**: This tool is not compliant with securities regulations (e.g., SEC, FINRA). Do not use for professional equity research without proper compliance review.

6. **Model Limitations**: AI models can produce biased, incorrect, or hallucinated outputs. Always verify information independently.

**Use at your own risk.** The developers, contributors, and affiliated parties disclaim all liability for damages resulting from the use of this software.

---

## 📞 Contact & Support

- **Issues**: Report bugs via GitHub Issues (if applicable)
- **Questions**: Open a discussion thread
- **Feature Requests**: Submit via Issues with "enhancement" label
- **Security Concerns**: Contact maintainer privately

---

## 🙏 Acknowledgments

- **Google Cloud**: For Vertex AI and Gemini API
- **React Team**: For the React framework
- **Tailwind Labs**: For Tailwind CSS
- **Open Source Community**: For inspiration and tools

---

## 📚 Additional Resources

- [Google Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Gemini API Reference](https://ai.google.dev/docs)
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)

---

**Built with ❤️ using Google Gemini AI**

*Last Updated: December 27, 2024*
