from fastapi import APIRouter
from app.models.schemas import Reporequest

router=APIRouter()
@router.post("/analyze")
def analyze_repo(request:):
    return {
        "message" : "analyze route is working"
    }