from newspaper import Article
import feedparser
import requests

def news_collector(url_dict: dict) -> list[dict]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    news_data = []

    for source, url in url_dict.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                feed = feedparser.parse(response.content)
                print(f"[{source}] Feed entries: {len(feed.entries)}")

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
                        print(f"[{source}] Failed to parse article: {e}")

                    news_data.append(article_info)
            else:
                print(f"[{source}] HTTP status not OK: {response.status_code}")
        except Exception as e:
            print(f"[{source}] Error fetching/parsing feed: {e}")
            continue  # Don't return, just skip this feed

    return news_data
