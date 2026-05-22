'use client';

import { SearchResult } from '@/lib/api';

interface ResultsListProps {
  results: SearchResult[];
  query: string;
  loading?: boolean;
}

export default function ResultsList({
  results,
  query,
  loading = false,
}: ResultsListProps) {
  if (loading) {
    return (
      <div className="max-w-3xl mx-auto my-10 px-5">
        <div className="text-center py-10 text-gray-500 text-base">
          Loading results...
        </div>
      </div>
    );
  }

  if (!query) {
    return null;
  }

  if (results.length === 0) {
    return (
      <div className="max-w-3xl mx-auto my-10 px-5">
        <div className="text-center py-10 text-gray-400 text-lg">
          No results found for "{query}"
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto my-10 px-5">
      <div className="mb-5 text-gray-600 text-sm">
        Found {results.length} results
      </div>
      <div className="flex flex-col gap-5">
        {results.map((result, index) => (
          <div
            key={index}
            className="p-4 border border-gray-300 rounded-lg transition-all duration-200 hover:bg-gray-50 hover:shadow-md"
          >
            <h3 className="m-0 mb-2 text-lg font-semibold">
              <a
                href={result.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-700 no-underline hover:underline"
              >
                {result.title}
              </a>
            </h3>
            <p className="m-0 mb-2 text-green-700 text-sm font-mono break-all">
              {result.url}
            </p>
            <p className="m-0 text-gray-600 text-sm leading-6">
              {result.snippet}
            </p>
            {result.score && (
              <p className="mt-2 text-gray-400 text-xs">
                Score: {result.score.toFixed(2)}
              </p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
