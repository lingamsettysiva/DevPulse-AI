from fastapi import FastAPIRouter

router=FastAPIRouter()
@router.get("/analyze")
def analyze():
    return {
        "message" 
    }