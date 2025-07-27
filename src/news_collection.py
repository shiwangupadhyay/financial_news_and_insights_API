from newspaper import Article
import feedparser
import requests
from config.constants.constant import URLs


def news_collector(url_dict: dict) -> list[dict]:
    """
    This function collects news articles with their title and other metadata from different news sites.

    Args:
        url_dict (dict): a dictionary of RSS URLs of different news sites keyed by name of source.

    Returns:
        list[dict]: list containing different news articles with metadata, each news is combined as a dictionary.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    news_data = []

    for source, url in url_dict.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                for entry in feed.entries[:10]:
                    article_info = {
                        "source": source,
                        "title": entry.title,
                        "url": entry.link,
                        "published": entry.get("published", "")
                    }

                    try:
                        article = Article(entry.link)
                        article.download()
                        article.parse()
                        article_info["content"] = article.text.strip()
                    except Exception as e:
                        article_info["content"] = "Failed to parse article."

                    news_data.append(article_info)
            else:
                return "failed to fetch news data"
        except Exception as e:
            return f"Error fetching/parsing {source}: {e}"
    
    return news_data