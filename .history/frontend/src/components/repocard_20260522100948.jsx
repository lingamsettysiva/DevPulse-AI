const RepoCard = ({ repository }) => {

  return (
    <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 shadow-lg">

      <h2 className="text-2xl font-bold mb-4">
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

    </div>
  );
};

export default RepoCard;