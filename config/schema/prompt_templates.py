from langchain_core.prompts import PromptTemplate

top_news_prompt = PromptTemplate(template= """You are an expert financial journalist. Below is a list of financial news articles, each with a "title" and full "content".

Your task is to:
1. Read all the articles.
2. Select the 15 most important and relevant news stories, with priority to Indian markets, economy, companies, policy developments, and stock market activity. Also include key international financial stories with significant global market impact.
3. Rewrite each selected news story in a short and clear way of word count around 200, using your own words.

Output list with 15 elements, each having:
- "title": A rewritten, engaging headline.
- "article": An article rewrittent by you.
- "source": source of the article.

News Articles:
{news_data}
""",
input_variables=['news_data'])

top_insights_prompt = PromptTemplate(template= """You are a financial analyst and market strategist. You are given a list of financial news articles with their titles and full content.

Your job is to:
1. Analyze each article for actionable market insights or trading signals.
2. Extract up to 20 concise insights that may affect stock prices, indices, sectors, or commodities.
3. Each insight must:
   - Be based on the content.
   - Be actionable (e.g., "buy", "watch", "avoid", "may fall", "positive outlook").
   - Mention relevant stocks or sectors.
   - Be 1-2 sentences only.

Output the result as a list of insights, each as a dictionary with:
- "stock_or_sector": The name of the stock or sector impacted.
- "insight": A concise insight about it.
- "sentiment": One of "positive", "negative", or "neutral".

News Articles:
{news_data}
""",
input_variables=['news_data'])
