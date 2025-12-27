
import React from 'react';
import type { AnalysisResult, FinancialMetric } from '../types';
import { ArrowDownRightIcon, ArrowUpRightIcon, MinusIcon, TrendingUpIcon, TrendingDownIcon, ScaleIcon, ShieldCheckIcon, LightbulbIcon, ExternalLinkIcon } from './icons';

interface AnalysisDashboardProps {
  result: AnalysisResult;
  onReset: () => void;
}

const getChangeColor = (change: string) => {
  if (change.startsWith('-')) return 'text-red-600';
  if (change !== 'N/A' && change !== '0.00%') return 'text-green-600';
  return 'text-gray-500';
};

const getChangeIcon = (change: string) => {
  if (change.startsWith('-')) return <ArrowDownRightIcon className="w-4 h-4" />;
  if (change !== 'N/A' && change !== '0.00%') return <ArrowUpRightIcon className="w-4 h-4" />;
  return <MinusIcon className="w-4 h-4" />;
};

const RecommendationBadge: React.FC<{ recommendation: 'BUY' | 'HOLD' | 'SELL' }> = ({ recommendation }) => {
  const baseClasses = "px-4 py-1 text-sm font-bold rounded-full inline-block";
  const styles = {
    BUY: "bg-green-100 text-green-800",
    HOLD: "bg-yellow-100 text-yellow-800",
    SELL: "bg-red-100 text-red-800",
  };
  return <span className={`${baseClasses} ${styles[recommendation]}`}>{recommendation}</span>;
};

export const AnalysisDashboard: React.FC<AnalysisDashboardProps> = ({ result, onReset }) => {
  return (
    <div className="space-y-8">
      <div className="flex justify-between items-start">
        <div>
          <h2 className="text-3xl font-bold text-gray-900">{result.companyName} ({result.tickerSymbol})</h2>
          <p className="text-lg text-gray-600">Analysis for {result.period}</p>
        </div>
        <button
          onClick={onReset}
          className="bg-white border border-gray-300 text-gray-700 font-semibold py-2 px-4 rounded-lg hover:bg-gray-50 transition-colors"
        >
          Analyze Another Report
        </button>
      </div>

      {/* Executive Summary */}
      <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
        <h3 className="text-xl font-semibold text-gray-800 mb-3">Executive Summary</h3>
        <p className="text-gray-600 whitespace-pre-wrap">{result.executiveSummary}</p>
      </section>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          {/* Financial Highlights */}
          <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h3 className="text-xl font-semibold text-gray-800 mb-4">Financial Highlights</h3>
            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-gray-200">
                    <th className="py-2 px-4 font-semibold text-gray-600 text-sm">Metric</th>
                    <th className="py-2 px-4 font-semibold text-gray-600 text-sm text-right">Value</th>
                    <th className="py-2 px-4 font-semibold text-gray-600 text-sm text-right">YoY Change</th>
                    <th className="py-2 px-4 font-semibold text-gray-600 text-sm text-right">QoQ Change</th>
                  </tr>
                </thead>
                <tbody>
                  {result.financials.map((metric: FinancialMetric, index: number) => (
                    <tr key={index} className="border-b border-gray-100 last:border-b-0">
                      <td className="py-3 px-4 font-medium text-gray-800">{metric.name}</td>
                      <td className="py-3 px-4 text-gray-800 font-mono text-right">{metric.value}</td>
                      <td className={`py-3 px-4 font-mono text-right ${getChangeColor(metric.yoyChange)}`}>
                        <span className="flex items-center justify-end gap-1">{getChangeIcon(metric.yoyChange)} {metric.yoyChange}</span>
                      </td>
                      <td className={`py-3 px-4 font-mono text-right ${getChangeColor(metric.qoqChange)}`}>
                        <span className="flex items-center justify-end gap-1">{getChangeIcon(metric.qoqChange)} {metric.qoqChange}</span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>

          {/* Risk Assessment */}
          <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h3 className="text-xl font-semibold text-gray-800 mb-4">Risk Assessment</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <h4 className="flex items-center gap-2 font-semibold text-red-700 mb-3"><TrendingDownIcon className="w-5 h-5" />Risks (Headwinds)</h4>
                <ul className="space-y-4">
                  {result.risks.risks.map((item, i) => (
                    <li key={i} className="text-sm">
                      <p className="font-semibold text-gray-800">{item.risk}</p>
                      <p className="text-gray-600"><strong>Mitigation:</strong> {item.mitigation}</p>
                    </li>
                  ))}
                </ul>
              </div>
              <div>
                <h4 className="flex items-center gap-2 font-semibold text-green-700 mb-3"><LightbulbIcon className="w-5 h-5" />Catalysts (Tailwinds)</h4>
                <ul className="space-y-4">
                  {result.risks.catalysts.map((item, i) => (
                    <li key={i} className="text-sm">
                      <p className="font-semibold text-gray-800">{item.catalyst}</p>
                      <p className="text-gray-600"><strong>Impact:</strong> {item.impact}</p>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </section>
        </div>

        <div className="space-y-8">
          {/* Stock Recommendation */}
          <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800 mb-4"><ScaleIcon className="w-6 h-6" />Stock Recommendation</h3>
            <div className="text-center mb-4">
              <RecommendationBadge recommendation={result.recommendation.recommendation} />
            </div>
            <p className="text-sm text-gray-600 italic mb-4">{result.recommendation.rationale}</p>
            <div className="space-y-3">
              <div>
                <h5 className="font-semibold text-green-700 text-sm mb-1">Bullish Points</h5>
                <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                  {result.recommendation.bullishPoints.map((pt, i) => <li key={i}>{pt}</li>)}
                </ul>
              </div>
              <div>
                <h5 className="font-semibold text-red-700 text-sm mb-1">Bearish Points</h5>
                <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                  {result.recommendation.bearishPoints.map((pt, i) => <li key={i}>{pt}</li>)}
                </ul>
              </div>
            </div>
          </section>

          {/* Forecasts */}
          <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800 mb-4"><TrendingUpIcon className="w-6 h-6" />Forecasts</h3>
            <div className="space-y-4">
              <div>
                <h4 className="text-sm font-semibold text-gray-500">Next Quarter</h4>
                <p className="text-lg font-semibold text-gray-800">Revenue: {result.forecast.nextQuarter.revenue}</p>
                <p className="text-lg font-semibold text-gray-800">EPS: {result.forecast.nextQuarter.eps}</p>
              </div>
              <div>
                <h4 className="text-sm font-semibold text-gray-500">12-Month Price Target</h4>
                <p className="text-2xl font-bold text-blue-600">{result.forecast.priceTarget12Month}</p>
              </div>
              <div>
                <h5 className="font-semibold text-gray-800 text-sm mb-1">Key Assumptions</h5>
                <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                  {result.forecast.assumptions.map((a, i) => <li key={i}>{a}</li>)}
                </ul>
              </div>
            </div>
          </section>

          {/* Competitive Positioning */}
          <section className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h3 className="flex items-center gap-2 text-xl font-semibold text-gray-800 mb-4"><ShieldCheckIcon className="w-6 h-6" />Competitive Positioning</h3>
            <p className="text-sm text-gray-600 mb-4">{result.competition.summary}</p>
            {result.competition.sources.length > 0 && (
              <div>
                <h5 className="font-semibold text-gray-800 text-sm mb-2">Sources</h5>
                <ul className="space-y-1">
                  {result.competition.sources.map((s, i) => (
                    <li key={i}>
                      <a href={s.uri} target="_blank" rel="noopener noreferrer" className="text-sm text-blue-600 hover:underline flex items-center gap-1">
                        {s.title} <ExternalLinkIcon className="w-3 h-3" />
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </section>
        </div>
      </div>
    </div>
  );
};
