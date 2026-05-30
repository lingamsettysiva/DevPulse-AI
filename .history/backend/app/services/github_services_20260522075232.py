from github import Github #communicate woth github ApI

def get_repo_details(repo_url:str):
    repo_url=repo_url.rstrip("/") #remove xtra space and take repo as a url
    

    repo_name = "/".join(repo_url.split("/")[-2:])
    
    g=Github()
    
    repo=g.get_repo(repo_name)
    
    return {
        "name": repo.name,
        "owner": repo.owner.login,
        "stars": repo.stargazers_count,
        "forks": repo.forks_count,
        "open_issues": repo.open_issues_count,
        "watchers": repo.watchers_count,
        "language": repo.language
    }