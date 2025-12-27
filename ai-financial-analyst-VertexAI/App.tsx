
import React, { useState, useCallback } from 'react';
import { FileUpload } from './components/FileUpload';
import { AnalysisProgress } from './components/AnalysisProgress';
import { AnalysisDashboard } from './components/AnalysisDashboard';
import { Header } from './components/Header';
import { ErrorDisplay } from './components/ErrorDisplay';
import { useFinancialAnalysis } from './hooks/useFinancialAnalysis';
import type { AnalysisResult } from './types';

type AnalysisState = 'idle' | 'analyzing' | 'success' | 'error';

export default function App() {
  const [analysisState, setAnalysisState] = useState<AnalysisState>('idle');
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  
  const { analyze, progress } = useFinancialAnalysis();

  const handleFileAnalysis = useCallback(async (file: File) => {
    setAnalysisState('analyzing');
    setError(null);
    setAnalysisResult(null);

    try {
      const result = await analyze(file);
      setAnalysisResult(result);
      setAnalysisState('success');
    } catch (err) {
      console.error(err);
      setError(err instanceof Error ? err.message : 'An unknown error occurred during analysis.');
      setAnalysisState('error');
    }
  }, [analyze]);

  const handleReset = () => {
    setAnalysisState('idle');
    setAnalysisResult(null);
    setError(null);
  };

  const renderContent = () => {
    switch (analysisState) {
      case 'idle':
        return <FileUpload onFileUpload={handleFileAnalysis} />;
      case 'analyzing':
        return <AnalysisProgress progress={progress} />;
      case 'success':
        return analysisResult ? <AnalysisDashboard result={analysisResult} onReset={handleReset} /> : <ErrorDisplay error="Analysis finished but no data was returned." onReset={handleReset} />;
      case 'error':
        return <ErrorDisplay error={error} onReset={handleReset} />;
      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <main className="container mx-auto px-4 py-8 md:py-12">
        <div className="max-w-5xl mx-auto">
          {renderContent()}
        </div>
      </main>
      <footer className="text-center py-4 text-sm text-gray-500">
        <p>Powered by Gemini. For informational purposes only. Not financial advice.</p>
      </footer>
    </div>
  );
}
