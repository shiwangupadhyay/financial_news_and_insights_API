from pydantic import BaseModel, Field
from typing import List

class NewsItem(BaseModel):
    """Represents a top financial news article."""
    title: str = Field(description="The title of the news article.")
    article: str = Field(description="A rewritten article by AI.")
    source: str = Field(description="The name of the news source (e.g., Economic Times, CNBC).")

class TopNewsResponse(BaseModel):
    """The response model for the Get Top News endpoint."""
    top_news: List[NewsItem] = Field(
        description="A list of the top 15 most relevant and recent financial news articles."
    )

class NewsInsight(BaseModel):
    """Represents a financial insight"""
    stock_or_sector: str =  Field(description="The name of the stock or sector impacted.")
    insight: str = Field(description= "A concise insight about it.")
    sentiment: str = Field(description="One of positive, negative, or neutral")

class NewsInsightResponse(BaseModel):
    """The response model for the Get news insights."""
    top_news: List[NewsInsight] = Field(
        description="A list of the top 20 concise insights that may affect stock prices, indices, sectors, or commodities."
    )