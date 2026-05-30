from github import Github #communicate woth github Api

def git_repo_details(repo_url:str):
    repo_url=repo_url.rstrip("/")