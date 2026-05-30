from fastapi import APIRouter
from fastapi.import 

router=APIRouter()
@router.get("/analyze")
def analyze():
    return {
        "message" : "analyze route is working"
    }