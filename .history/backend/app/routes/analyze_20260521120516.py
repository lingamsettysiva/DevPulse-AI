from fastapi import APIRouter
from app.models.schemas import Reporequest

router=APIRouter()
@router.post("/analyze")
def analyze_repo(request: RepoRequest):
    return {
        "repo_url": request.repo_url,
        "message": "Repository received successfully"
    }