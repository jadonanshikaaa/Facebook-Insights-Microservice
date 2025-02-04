from fastapi import FastAPI
from app.routes.pages import router

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Facebook Insights API"}
