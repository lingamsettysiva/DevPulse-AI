from fastapi import APIRouter
from app.model.schemas import RepoRequest
from app.services.github_services import get_repo_details
from app.services.metrics_services import 

router = APIRouter()


@router.post("/analyze")
def analyze_repo(request: RepoRequest):

    repo_data = get_repo_details(request.repo_url)

    return {
        "success": True,
        "data": repo_data
    }