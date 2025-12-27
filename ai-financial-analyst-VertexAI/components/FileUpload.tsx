
import React, { useState, useCallback } from 'react';
import { UploadCloudIcon, FileIcon } from './icons';

interface FileUploadProps {
  onFileUpload: (file: File) => void;
}

export const FileUpload: React.FC<FileUploadProps> = ({ onFileUpload }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (files: FileList | null) => {
    if (files && files[0]) {
      if (files[0].type === 'application/pdf') {
        setFile(files[0]);
        setError(null);
      } else {
        setError('Invalid file type. Please upload a PDF.');
        setFile(null);
      }
    }
  };

  const handleDragEnter = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    handleFileChange(e.dataTransfer.files);
  };

  const handleSubmit = () => {
    if (file) {
      onFileUpload(file);
    } else {
      setError('Please select a file to analyze.');
    }
  };

  return (
    <div className="bg-white p-8 rounded-lg shadow-md border border-gray-200 text-center">
      <h2 className="text-2xl font-semibold text-gray-800 mb-2">Upload Earnings Report</h2>
      <p className="text-gray-500 mb-6">Upload a corporate earnings report in PDF format to begin your analysis.</p>
      
      <div
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        className={`relative border-2 border-dashed rounded-lg p-10 transition-colors duration-200 ${isDragging ? 'border-blue-500 bg-blue-50' : 'border-gray-300 bg-gray-50'}`}
      >
        <input
          type="file"
          id="file-upload"
          className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
          accept="application/pdf"
          onChange={(e) => handleFileChange(e.target.files)}
          aria-label="Upload PDF file"
        />
        <div className="flex flex-col items-center justify-center space-y-4 text-gray-500">
          <UploadCloudIcon className="w-12 h-12" />
          <p className="font-semibold">
            <label htmlFor="file-upload" className="text-blue-600 hover:text-blue-700 cursor-pointer font-semibold">Click to upload</label> or drag and drop
          </p>
          <p className="text-sm">PDF only, up to 10MB</p>
        </div>
      </div>

      {error && <p className="mt-4 text-sm text-red-600">{error}</p>}

      {file && (
        <div className="mt-6 text-left bg-gray-100 p-4 rounded-lg flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <FileIcon className="w-6 h-6 text-gray-500" />
            <span className="text-sm font-medium text-gray-700">{file.name}</span>
          </div>
          <button onClick={() => setFile(null)} className="text-gray-500 hover:text-gray-700 text-sm font-semibold">Remove</button>
        </div>
      )}

      <button
        onClick={handleSubmit}
        disabled={!file}
        className="mt-8 w-full bg-blue-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
        aria-disabled={!file}
      >
        Analyze Report
      </button>
    </div>
  );
};
