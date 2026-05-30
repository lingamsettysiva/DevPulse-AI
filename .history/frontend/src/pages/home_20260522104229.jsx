import { useState } from "react";

import SearchBar from "../components/SearchBar";

import RepoCard from "../components/RepoCard";
import MetricsCard from "../components/MetricsCard";
import PredictionCard from "../components/PredictionCard";
import AIReport from "../components/AIReport";
import Navbar from "../components/Navbar";
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
  <div className="min-h-screen bg-black text-white p-10">

    <div className="max-w-6xl mx-auto">

      <Navbar />

      <div className="bg-zinc-900 p-6 rounded-2xl shadow-xl">

        <SearchBar onAnalyze={handleAnalyze} />

      </div>

      {loading && (

  <div className="flex justify-center mt-10">

    <div className="animate-spin rounded-full h-16 w-16 border-b-4 border-cyan-400">
    </div>

  </div>

)}

      {result && (

        <div className="grid md:grid-cols-2 gap-6 mt-10">

          <RepoCard repository={result.repository} />

          <MetricsCard metrics={result.metrics} />

          <PredictionCard
            prediction={result.ml_prediction}
          />

          <AIReport report={result.ai_report} />
          <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

  <h2 className="text-2xl font-bold mb-4 text-cyan-400">
    Retrieved Engineering Knowledge
  </h2>

  <ul className="list-disc pl-6 text-gray-300">

    {result.rag_context.map((item, index) => (

      <li key={index}>
        {item}
      </li>

    ))}

  </ul>

</div>

        </div>

      )}

    </div>

  </div>
);
};

export default Home;