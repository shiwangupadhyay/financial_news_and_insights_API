from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config.constants import API_VERSION

app = FastAPI(
    title="AI-Powered Financial News and Insights API",
    version=API_VERSION,
    description="Get summarized financial news and market insights generated using Gen AI"
)

@app.get("/", status_code=200)
def root():
    return {"message": "Welcome to the AI-powered Financial News Aggregator and Insights API."}

@app.get("/about", status_code=200)
def about():
    return {
        "message": "This API provides top financial news summaries and AI-generated market insights based on current headlines."
    }

@app.get("/health", status_code=200)
def health():
    return {
        "status": "OK",
        "version": API_VERSION
    }


@app.get("/get_top_news")
def get_top_news():
    pass