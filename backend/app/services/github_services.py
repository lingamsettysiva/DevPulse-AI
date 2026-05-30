from github import Github


def check_for_tests(repo, path=""):

    test_keywords = [
        "test",
        "tests",
        "__tests__",
        "spec",
        "specs"
    ]

    try:

        contents = repo.get_contents(path)

        for content in contents:

            name = content.name.lower()

            # Check file/folder names
            if any(
                keyword in name
                for keyword in test_keywords
            ):

                return True

            # Recursive folder scan
            if content.type == "dir":

                if check_for_tests(
                    repo,
                    content.path
                ):

                    return True

    except Exception:

        pass

    return False


def get_repo_details(repo_url: str):

    repo_url = repo_url.rstrip("/")

    repo_name = "/".join(
        repo_url.split("/")[-2:]
    )

    g = Github()

    repo = g.get_repo(repo_name)

    # Root contents
    contents = repo.get_contents("")

    file_names = [
        content.name.lower()
        for content in contents
    ]

    # Recursive test detection
    has_tests = check_for_tests(repo)

    return {
        "name": repo.name,
        "owner": repo.owner.login,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "open_issues": repo.open_issues_count,
        "watchers": repo.watchers_count,
        "language": repo.language,

        # Intelligent checks
        "has_readme":
            "readme.md" in file_names,

        "has_license":
            "license" in file_names
            or "license.md" in file_names,

        "has_tests": has_tests
    }