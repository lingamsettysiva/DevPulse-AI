from github import Github


def get_repo_details(repo_url: str):

    repo_url = repo_url.rstrip("/")

    repo_name = "/".join(
        repo_url.split("/")[-2:]
    )

    g = Github()

    repo = g.get_repo(repo_name)

    # Fetch root files/folders
    contents = repo.get_contents("")

    file_names = [
        content.name.lower()
        for content in contents
    ]

    return {
        "name": repo.name,
        "owner": repo.owner.login,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "open_issues": repo.open_issues_count,
        "watchers": repo.watchers_count,
        "language": repo.language,

        # New intelligent checks
        "has_readme":
            "readme.md" in file_names,

        "has_license":
            "license" in file_names
            or "license.md" in file_names,

        # Better test detection
test_keywords = [
    "test",
    "tests",
    "__tests__",
    "spec",
    "specs"
]

has_tests = False

for content in contents:

    name = content.name.lower()

    if any(
        keyword in name
        for keyword in test_keywords
    ):

        has_tests = True
        break
    }