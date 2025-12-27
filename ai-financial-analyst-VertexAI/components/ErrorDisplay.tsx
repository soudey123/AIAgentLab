
import React from 'react';
import { AlertTriangleIcon } from './icons';

interface ErrorDisplayProps {
  error: string | null;
  onReset: () => void;
}

export const ErrorDisplay: React.FC<ErrorDisplayProps> = ({ error, onReset }) => {
  return (
    <div className="bg-red-50 border-l-4 border-red-500 text-red-800 p-6 rounded-lg shadow-md text-center" role="alert">
      <div className="flex flex-col items-center">
        <AlertTriangleIcon className="w-12 h-12 text-red-500 mb-4" />
        <h3 className="text-xl font-bold mb-2">Analysis Failed</h3>
        <p className="mb-6 text-sm">
          {error || 'An unexpected error occurred. Please check the console for more details.'}
        </p>
        <button
          onClick={onReset}
          className="bg-red-600 text-white font-bold py-2 px-6 rounded-lg hover:bg-red-700 transition-colors"
        >
          Try Again
        </button>
      </div>
    </div>
  );
};
