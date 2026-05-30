from github import Github #communicate woth github ApI

def git_repo_details(repo_url:str):
    repo_url=repo_url.rstrip("/") #remove xtra space and take repo as a url
    

    repo_name = "/".join(repo_url.split("/")[-2:])
    
    g=github()