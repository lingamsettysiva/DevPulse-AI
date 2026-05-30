from fastapi import APIRouter
from app.model.schemas import RepoRequest
from app.services.github_service import get_repo_details

router = APIRouter()


@router.post("/analyze")
def analyze_repo(request: RepoRequest):

    repo_data = get_repo_details(request.repo_url)

    return {
        "success": True,
        "data": repo_data
    }