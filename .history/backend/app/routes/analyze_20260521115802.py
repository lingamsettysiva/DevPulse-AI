from fastapi import APIRouter

router=APIRouter()
@router.get("/analyze")
def analyze():
    return {
        "message" : "analyze route is working"
    }