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

    # Fetch repository details
    repo_data = get_repo_details(request.repo_url)

    # Calculate repository metrics
    metrics = calculate_repo_metrics(repo_data)

    # ML prediction
    prediction = predict_repository_risk(metrics)

    # Store documents only once
    store_documents()

    # Better RAG query
    query = f"""
    Repository Name: {repo_data["name"]}
    Language: {repo_data["language"]}
    Open Issues: {repo_data["open_issues"]}
    Risk Level: {metrics["risk_level"]}
    Prediction: {prediction["prediction"]}
    """

    # Retrieve relevant engineering context
    rag_context = retrieve_relevant_context(query)

    # Debug retrieved context
    print(rag_context)

    # Generate AI report
    ai_report = generate_ai_report(
        repo_data,
        metrics,
        prediction,
        rag_context
    )

    return {
        "success": True,
        "repository": repo_data,
        "metrics": metrics,
        "ml_prediction": prediction,
        "rag_context": rag_context,
        "ai_report": ai_report
    }