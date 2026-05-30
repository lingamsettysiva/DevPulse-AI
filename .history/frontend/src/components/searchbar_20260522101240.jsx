import { useState } from "react";

const SearchBar = ({ onAnalyze }) => {

  const [repoUrl, setRepoUrl] = useState("");

  const handleSubmit = () => {

    if (!repoUrl) return;

    onAnalyze(repoUrl);
  };

  return (
    <div className="flex gap-4">

      <input
        type="text"
        placeholder="Enter GitHub Repository URL"
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
        className="bg-zinc-800 border border-zinc-700 p-4 rounded-xl w-full text-white outline-none"
      />

      <button
        onClick={handleSubmit}
        className="bg-cyan-500 hover:bg-cyan-400 transition px-6 rounded-xl font-semibold"
      >
        Analyze
      </button>

    </div>
  );
};

export default SearchBar;