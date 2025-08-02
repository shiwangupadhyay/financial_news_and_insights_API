import yfinance as yf


def indices_data(symbols: dict) -> dict:
    """Fetches Live price data for indices like Nifty, Sensex etc from yfinance.

    Args:
        symbol (dict): Dictionary of indices name as key and their symbols as values.

    Returns:
        dict: a dictionary of name, symbol, price, change, percent_change of input symbols.
    """
    data = {}
    for name, symbol in symbols.items():
        try:
            ticker = yf.Ticker(symbol)
            price = ticker.info.get("regularMarketPrice")
            change = ticker.info.get("regularMarketChange")
            percent = ticker.info.get("regularMarketChangePercent")

            data[name] = {
                "symbol": symbol,
                "price": round(price,2),
                "change": round(change,2),
                "percent_change": round(percent,2),
            }
        except Exception as e:
            return f"Indices data can not be collected {e}"
    return data