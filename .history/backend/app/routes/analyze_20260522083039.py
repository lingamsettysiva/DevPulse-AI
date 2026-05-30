from fastapi import APIRouter
from app.model.schemas import RepoRequest
from app.services.github_services import get_repo_details
from app.services.metrics_service import calculate_repo_metrics
from app.services.ml_service import calculate_repo_metrics
router = APIRouter()


@router.post("/analyze")
def analyze_repo(request: RepoRequest):

    repo_data = get_repo_details(request.repo_url)
    
    metrics=calculate_repo_metrics(repo_data)

    prediction = predict_repository_risk(metrics)
    return {
        "success": True,
        "repository": repo_data,
        "metrics": metrics
        "ml_prediction"
    }