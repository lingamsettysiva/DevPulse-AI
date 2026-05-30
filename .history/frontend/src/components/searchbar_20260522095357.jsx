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
        className="border p-3 rounded-lg w-full"
      />

      <button
        onClick={handleSubmit}
        className="bg-black text-white px-6 rounded-lg"
      >
        Analyze
      </button>

    </div>
  );
};

export default SearchBar;