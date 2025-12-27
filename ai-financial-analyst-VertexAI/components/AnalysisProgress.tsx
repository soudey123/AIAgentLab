
import React from 'react';
import { LoaderCircleIcon } from './icons';

interface AnalysisProgressProps {
  progress: string;
}

export const AnalysisProgress: React.FC<AnalysisProgressProps> = ({ progress }) => {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md border border-gray-200 text-center flex flex-col items-center justify-center min-h-[400px]">
      <LoaderCircleIcon className="w-16 h-16 text-blue-600 animate-spin mb-6" />
      <h2 className="text-2xl font-semibold text-gray-800 mb-2">Analyzing Report...</h2>
      <p className="text-gray-500 max-w-md">{progress || 'Initializing analysis engine. This may take a moment.'}</p>
    </div>
  );
};
