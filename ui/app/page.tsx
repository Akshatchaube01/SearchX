'use client';

import { useState } from 'react';
import SearchBar from '@/components/SearchBar';
import ResultsList from '@/components/ResultsList';
import { searchAPI, SearchResult } from '@/lib/api';

export default function Home() {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (searchQuery: string) => {
    setQuery(searchQuery);
    setLoading(true);
    setError(null);

    try {
      const response = await searchAPI.search(searchQuery);
      setResults(response.results);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'An error occurred while searching. Make sure the API is running.'
      );
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex-1 w-full flex flex-col justify-start">
      <div className="text-center py-16 px-5">
        <h1 className="text-5xl font-bold mb-2 text-gray-900">SearchX</h1>
        <p className="text-base font-light text-gray-600">A modern search engine</p>
      </div>

      <SearchBar onSearch={handleSearch} isLoading={loading} />

      {error && (
        <div className="max-w-3xl mx-auto my-5 px-4 py-4 bg-red-50 text-red-700 border border-red-300 rounded-lg text-sm">
          {error}
        </div>
      )}

      <ResultsList results={results} query={query} loading={loading} />

      {!query && !loading && (
        <div className="text-center py-20 px-5 text-gray-500 text-lg">
          <p>Start typing to search the web...</p>
        </div>
      )}
    </main>
  );
}
