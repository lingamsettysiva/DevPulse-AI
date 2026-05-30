const RepoCard = ({ repository }) => {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4 text-cyan-400">
        Repository Info
      </h2>

      <p>
        <strong>Name:</strong> {repository.name}
      </p>

      <p>
        <strong>Owner:</strong> {repository.owner}
      </p>

      <p>
        <strong>Stars:</strong> {repository.stars}
      </p>

      <p>
        <strong>Forks:</strong> {repository.forks}
      </p>

      <p>
        <strong>Language:</strong> {repository.language}
      </p>

      <p>
  <strong>README:</strong>
  {" "}
  {repository.has_readme ? "Yes" : "No"}
</p>

<p>
  <strong>License:</strong>
  {" "}
  {repository.has_license ? "Yes" : "No"}
</p>

<p>
  <strong>Tests:</strong>
  {" "}
  {repository.has_tests ? "Yes" : "No"}
</p>

    </div>
  );
};

export default RepoCard;