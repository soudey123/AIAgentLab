
import React from 'react';
import { BrainCircuitIcon } from './icons';

export const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-sm">
      <div className="container mx-auto px-4 py-4 flex items-center">
        <BrainCircuitIcon className="h-8 w-8 text-blue-600 mr-3" />
        <div>
          <h1 className="text-xl font-bold text-gray-900">AI Financial Analyst</h1>
          <p className="text-sm text-gray-500">Institutional-Grade Insights on Demand</p>
        </div>
      </div>
    </header>
  );
};
