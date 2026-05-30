from fastapi import APIRouter

router=FastAPIRouter()
@router.get("/analyze")
def analyze():
    return {
        "message" : "analyze route is working"
    }