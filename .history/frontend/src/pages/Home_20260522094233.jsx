import { useState } from "react";

import SearchBar from "../components/SearchBar";

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
    <div className="min-h-screen p-10 bg-gray-100">

      <h1 className="text-4xl font-bold mb-8">
        DevPulse AI
      </h1>

      <SearchBar onAnalyze={handleAnalyze} />

      {loading && (
        <p>Analyzing repository...</p>
      )}

      {result && (
        <div className="bg-white p-6 rounded-xl shadow-md mt-6">

          <h2 className="text-2xl font-bold mb-4">
            Repository Analysis
          </h2>

          <p>
            <strong>Name:</strong> {result.repository.name}
          </p>

          <p>
            <strong>Owner:</strong> {result.repository.owner}
          </p>

          <p>
            <strong>Stars:</strong> {result.repository.stars}
          </p>

          <p>
            <strong>Risk Level:</strong> {result.metrics.risk_level}
          </p>

          <p>
            <strong>Prediction:</strong> {result.ml_prediction.prediction}
          </p>

          <div className="mt-4">

            <h3 className="text-xl font-semibold mb-2">
              AI Report
            </h3>

            <p>
              {result.ai_report}
            </p>

          </div>

        </div>
      )}

    </div>
  );
};

export default Home;