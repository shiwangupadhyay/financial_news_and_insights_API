from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from config.constants.constant import API_VERSION, URLs, SYMBOLS
from config.schema.prompt_templates import top_insights_prompt, top_news_prompt
from src.models import news_llm, insight_llm
from src.news_collection import news_collector
from src.indices_data import indices_data
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(
    title="AI-Powered Financial News and Insights API",
    version=API_VERSION,
    description="Get summarized financial news and market insights generated using Gen AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    
    news_data = news_collector(url_dict=URLs)
    
    if not news_data:
        raise HTTPException(status_code=404,detail="Unable to fetch news data")

    try:
        model = top_news_prompt | news_llm

        response = model.invoke(news_data).top_news

        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred: {str(e)}"}
        )
    

@app.get("/get_news_insight")
def get_insight():
    
    news_data = news_collector(url_dict=URLs)
    
    if not news_data:
        raise HTTPException(status_code=404,detail="Unable to fetch news data")

    try:
        model = top_insights_prompt | insight_llm
        response = model.invoke(news_data).top_news

        return response
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred: {str(e)}"}
        )
    


@app.get("/indices_price_data")
def get_indices_data():
    
    price_data = indices_data(SYMBOLS)

    if not price_data:
        raise HTTPException(status_code=404,detail="Unable to fetch indices price data")

    return JSONResponse(status_code= 200,content= price_data)
        

