# FinIntel API: AI-Powered Financial News & Market Insights 🚀

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.35.0-orange.svg)](https://www.uvicorn.org/)

An intelligent FastAPI service providing real-time summarized financial news, AI-generated market insights, and live financial index data.

---

## ✨ Key Features

*   **AI-Powered News Summarization:** Get concise, rewritten summaries of top financial news articles from multiple prominent sources.
*   **Generative AI Market Insights:** Receive actionable insights derived from current news, highlighting potential impacts on stocks, sectors, and commodities, complete with sentiment analysis.
*   **Real-time Financial Indices:** Access up-to-the-minute price data for major global and Indian financial indices like NIFTY 50, SENSEX, BANK NIFTY, and currency pairs like USD/INR.
*   **Multi-Source News Aggregation:** Gathers and processes news from leading financial outlets including Economic Times, Business Standard, Livemint, and CNBC.
*   **Scalable & Containerized:** Comes with a `Dockerfile` for easy deployment, ensuring consistency across environments and simplifying scaling.
*   **OpenAPI Documentation:** Automatically generated interactive API documentation (Swagger UI) for seamless exploration and testing of endpoints.
*   **CORS Enabled:** Configured for Cross-Origin Resource Sharing, allowing easy integration with front-end applications.

## 📂 Project Structure

```
.
├── app.py                      # Main FastAPI application
├── Dockerfile                  # Docker configuration for containerization
├── LICENSE                     # Project license (MIT)
├── README.md                   # This README file
├── requirements.txt            # Python dependencies
├── config/                     # Configuration files
│   ├── __init__.py             # Python package marker
│   ├── constants/              # Global constants
│   │   ├── __init__.py         # Python package marker
│   │   └── constant.py         # API version, news URLs, and financial symbols
│   └── schema/                 # Pydantic models for API input/output
│       ├── __init__.py         # Python package marker
│       ├── output_schema.py    # Defines response structures for news and insights
│       └── prompt_templates.py # LangChain prompt templates for AI models
└── src/                        # Source code for core functionalities
    ├── __init__.py             # Python package marker
    ├── indices_data.py         # Logic for fetching live financial index data
    ├── models.py               # Initializes and configures LangChain AI models
    └── news_collection.py      # Handles news aggregation from RSS feeds
```

## 🛠️ Technologies Used

*   **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **AI/ML:** [LangChain](https://www.langchain.com/), [Google Gemini API (via `langchain-google-genai`)](https://ai.google.dev/models/gemini)
*   **Data Collection:** [Newspaper3k](https://newspaper.readthedocs.io/), [Feedparser](https://pypi.org/project/feedparser/), [Yfinance](https://pypi.org/project/yfinance/)
*   **Web Server:** [Uvicorn](https://www.uvicorn.org/)
*   **Dependency Management:** `pip`, `requirements.txt`
*   **Containerization:** [Docker](https://www.docker.com/)
*   **Environment Variables:** [python-dotenv](https://pypi.org/project/python-dotenv/)
*   **Language:** [Python 3.11+](https://www.python.org/)

## ⚙️ Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

*   Python 3.11+
*   `pip` (Python package installer)
*   A [Google Gemini API Key](https://ai.google.dev/gemini-api/docs/get-started/python)
*   (Optional, for Docker usage) Docker Desktop

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/shiwangupadhyay/financial_news_and_insights_API.git # Replace with actual repo URL if different
    cd financial_news_and_insights_API
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory of the project and add your Google Gemini API key:
    ```dotenv
    GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY_HERE
    ```
    *Replace `YOUR_GOOGLE_GEMINI_API_KEY_HERE` with your actual API key.*

## 🚀 Usage

### Running the Application Locally

Once the dependencies are installed and the `.env` file is set up, you can run the FastAPI application:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
The `--reload` flag is optional but useful for development, as it will automatically restart the server on code changes.

The API will be accessible at `http://127.0.0.1:8000`.

### Accessing API Documentation

After running the server, you can access the interactive API documentation (Swagger UI) at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Or the ReDoc documentation at:
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running with Docker

For a containerized setup, use the provided `Dockerfile`:

1.  **Build the Docker Image:**
    ```bash
    docker build -t finintel-api .
    ```

2.  **Run the Docker Container:**
    ```bash
    docker run -p 8000:8000 --env GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY_HERE finintel-api
    ```
    *Remember to replace `YOUR_GOOGLE_GEMINI_API_KEY_HERE` with your actual API key.*

The API will then be available at `http://localhost:8000`.

## 🌐 API Endpoints

The FinIntel API provides the following endpoints:

### 1. Root Endpoint

*   **URL:** `/`
*   **Method:** `GET`
*   **Description:** A simple welcome message to the API.
*   **Response:**
    ```json
    {
      "message": "Welcome to the AI-powered Financial News Aggregator and Insights API."
    }
    ```

### 2. About Endpoint

*   **URL:** `/about`
*   **Method:** `GET`
*   **Description:** Provides information about the API's purpose.
*   **Response:**
    ```json
    {
      "message": "This API provides top financial news summaries and AI-generated market insights based on current headlines."
    }
    ```

### 3. Health Check Endpoint

*   **URL:** `/health`
*   **Method:** `GET`
*   **Description:** Checks the health status and version of the API.
*   **Response:**
    ```json
    {
      "status": "OK",
      "version": "1.0.0"
    }
    ```

### 4. Get Top News

*   **URL:** `/get_top_news`
*   **Method:** `GET`
*   **Description:** Fetches, aggregates, and summarizes the top 15 most relevant financial news articles using AI.
*   **Response (JSON):** A list of news items, each with a rewritten title, summarized article content, and source.
    ```json
    {
      "top_news": [
        {
          "title": "Rewritten engaging headline 1",
          "article": "AI-generated summary of article 1, around 200 words.",
          "source": "economic_times"
        },
        {
          "title": "Rewritten engaging headline 2",
          "article": "AI-generated summary of article 2, around 200 words.",
          "source": "livemint_markets"
        }
        // ... up to 15 news items
      ]
    }
    ```

### 5. Get News Insight

*   **URL:** `/get_news_insight`
*   **Method:** `GET`
*   **Description:** Analyzes current news and generates up to 20 concise, actionable market insights that may affect stock prices, indices, sectors, or commodities, including sentiment.
*   **Response (JSON):** A list of insights.
    ```json
    {
      "top_news": [
        {
          "stock_or_sector": "Indian Banking Sector",
          "insight": "New RBI policies may lead to increased lending and improved profitability for public sector banks, indicating a positive outlook.",
          "sentiment": "positive"
        },
        {
          "stock_or_sector": "Tech Stocks",
          "insight": "Global tech slowdown concerns could temper investor sentiment, suggesting a cautious approach for tech-heavy portfolios.",
          "sentiment": "neutral"
        }
        // ... up to 20 insights
      ]
    }
    ```

### 6. Get Indices Price Data

*   **URL:** `/indices_price_data`
*   **Method:** `GET`
*   **Description:** Retrieves live price data for predefined financial indices (NIFTY 50, SENSEX, BANK NIFTY, NIFTY MIDCAP, USD/INR).
*   **Response (JSON):** A dictionary mapping index names to their current price, change, and percentage change.
    ```json
    {
      "NIFTY 50": {
        "symbol": "^NSEI",
        "price": 23558.00,
        "change": 78.00,
        "percent_change": 0.33
      },
      "SENSEX": {
        "symbol": "^BSESN",
        "price": 77337.59,
        "change": 254.59,
        "percent_change": 0.33
      },
      "BANK NIFTY": {
        "symbol": "^NSEBANK",
        "price": 50125.00,
        "change": 125.00,
        "percent_change": 0.25
      },
      "NIFTY MIDCAP": {
        "symbol": "^NSEMDCP50",
        "price": 14000.00,
        "change": 50.00,
        "percent_change": 0.36
      },
      "USD/INR": {
        "symbol": "USDINR=X",
        "price": 83.50,
        "change": -0.05,
        "percent_change": -0.06
      }
    }
    ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.