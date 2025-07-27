from langchain_google_genai import ChatGoogleGenerativeAI
from config.schema.output_schema import TopNewsResponse, NewsInsightResponse
from dotenv import load_dotenv

load_dotenv()

llm_news = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3
)

llm_insight = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.4
)

news_llm = llm_news.with_structured_output(TopNewsResponse)

insight_llm = llm_insight.with_structured_output(NewsInsightResponse)