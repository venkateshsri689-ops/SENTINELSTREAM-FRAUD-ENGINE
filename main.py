from fastapi import FastAPI
from app.api.routes.transaction import router as transaction_router

app =FastAPI(title="SentinelStream",
             description="High throughput fraud Detection Engine", version="1.0.0")
app.include_router(transaction_router,prefix="/api")
                   @app.get("/")
                   def health_check():
                       return {"status":"sentinelstream is running"}