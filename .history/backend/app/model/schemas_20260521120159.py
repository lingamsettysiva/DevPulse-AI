from pydantic import BaseModel # validation, request, response 

class RepoRequest(BaseModel):
    repo_url