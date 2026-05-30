import { useState } from "react";

import SearchBar from "../components/SearchBar";

import RepoCard from "../components/RepoCard";
import MetricsCard from "../components/MetricsCard";
import PredictionCard from "../components/PredictionCard";
import AIReport from "../components/AIReport";

import { analyzeRepository } from "../services/api";

const Home = () => {

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (repoUrl) => {

    try {

      setLoading(true);

      const data = await analyzeRepository(repoUrl);

      setResult(data);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <h1 className="text-5xl font-bold mb-8 text-center">
        DevPulse AI
      </h1>

      <SearchBar onAnalyze={handleAnalyze} />

      {loading && (
        <p className="mt-6 text-lg">
          Analyzing repository...
        </p>
      )}

      {result && (

        <div className="grid gap-6 mt-8">

          <RepoCard repository={result.repository} />

          <MetricsCard metrics={result.metrics} />

          <PredictionCard
            prediction={result.ml_prediction}
          />

          <AIReport report={result.ai_report} />

        </div>
      )}

    </div>
  );
};

export default Home;