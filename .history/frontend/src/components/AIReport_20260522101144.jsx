const AIReport = ({ report }) => {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4 text-cyan-400">
        AI Report
      </h2>

      <p className="leading-7 whitespace-pre-line text-gray-300">
        {report}
      </p>

    </div>
  );
};

export default AIReport;