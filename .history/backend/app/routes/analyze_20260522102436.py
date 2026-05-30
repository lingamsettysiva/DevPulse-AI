from fastapi import APIRouter
from app.model.schemas import RepoRequest
from app.services.github_services import get_repo_details
from app.services.metrics_service import calculate_repo_metrics
from app.services.ml_service import predict_repository_risk
from app.services.gemini_service import generate_ai_report
from app.services.rag_service import (
    store_documents,
    retrieve_relevant_context
)
router = APIRouter()


@router.post("/analyze")
def analyze_repo(request: RepoRequest):

    repo_data = get_repo_details(request.repo_url)
    
    metrics=calculate_repo_metrics(repo_data)

    prediction = predict_repository_risk(metrics)
    
    ai_report = generate_ai_report(
        repo_data,
        metrics,
        prediction
    )
    
    store_documents()

rag_context = retrieve_relevant_context(
    prediction["prediction"]
)
    return {
        "success": True,
        "repository": repo_data,
        "metrics": metrics,
        "ml_prediction":prediction,
        "ai_report": ai_report
    }