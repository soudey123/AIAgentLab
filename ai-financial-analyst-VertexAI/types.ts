
export interface FinancialMetric {
  name: string;
  value: string;
  yoyChange: string;
  qoqChange: string;
}

export interface CompetitiveAnalysis {
  summary: string;
  competitors: {
    name: string;
    notes: string;
  }[];
  sources: {
    title: string;
    uri: string;
  }[];
}

export interface StockRecommendation {
  recommendation: 'BUY' | 'HOLD' | 'SELL';
  rationale: string;
  bullishPoints: string[];
  bearishPoints: string[];
}

export interface Forecast {
  nextQuarter: {
    revenue: string;
    eps: string;
  };
  priceTarget12Month: string;
  assumptions: string[];
}

export interface RiskAssessment {
  risks: {
    risk: string;
    mitigation: string;
  }[];
  catalysts: {
    catalyst: string;
    impact: string;
  }[];
}

export interface AnalysisResult {
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
