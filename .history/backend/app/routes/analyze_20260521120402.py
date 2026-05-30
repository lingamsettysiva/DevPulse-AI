from fastapi import APIRouter
from app.models.schemas import Reporequest

router=APIRouter()
@router.get("/analyze")
def analyze():
    return {
        "message" : "analyze route is working"
    }