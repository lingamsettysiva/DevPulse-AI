from fastapi import APIRouter
from app.model.schemas import RepoRequest

router=APIRouter()
@router.post("/analyze")
def analyze_repo(request: RepoRequest): # we are getting request from the 
    return {
        "repo_url": request.repo_url,
        "message": "Repository received successfully" 
    }