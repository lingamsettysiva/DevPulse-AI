const MetricsCard = ({ metrics }) => {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4 text-cyan-400">
        Metrics
      </h2>

      <p>
        <strong>Popularity Score:</strong>
        {" "}
        {metrics.popularity_score}
      </p>

      <p>
        <strong>Risk Level:</strong>
        {" "}
        {metrics.risk_level}
      </p>

    </div>
  );
};

export default MetricsCard;