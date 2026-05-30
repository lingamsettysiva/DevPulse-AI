from fastapi import FastApI
from fastapi.middleware.cors import CORSMiddleware # connecting frotend to backend
from app.routes.analyze import router as analyze_router # api endpoints

app=FastApI( # cretes backend application apperas in locolhost
    title="Devpulse_AI"
    description="AI powered github repositiory analyzer"
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # allow all frontend apps
    allow_credentials=True,
    allow_methods=["*"] # allow get put 
)
