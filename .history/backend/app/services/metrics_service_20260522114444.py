def calculate_repo_metrics(repo_data):

    stars = repo_data["stars"]

    forks = repo_data["forks"]

    open_issues = repo_data["open_issues"]

    watchers = repo_data["watchers"]

    popularity_score = (
        stars + forks + watchers
    )

    # Risk calculation
    # Better risk calculation
    issue_ratio = open_issues / (stars + 1)

    if issue_ratio > 0.5:

      risk_level = "High"

    elif issue_ratio > 0.1:

      risk_level = "Medium"

    else:

    risk_level = "Low"

    # Weakness detection
    weaknesses = []

    if not repo_data["has_readme"]:

        weaknesses.append(
            "Repository lacks README documentation"
        )

    if not repo_data["has_license"]:

        weaknesses.append(
            "Repository has no license"
        )

    if not repo_data["has_tests"]:

        weaknesses.append(
            "Repository lacks testing structure"
        )

    return {
        "popularity_score": popularity_score,
        "risk_level": risk_level,
        "weaknesses": weaknesses
    }