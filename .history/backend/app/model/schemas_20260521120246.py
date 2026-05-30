from pydantic import BaseModel # validation, request, response 

class RepoRequest(BaseModel): # defines ApI request format
    repo_url: str #string t