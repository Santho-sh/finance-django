import os
import requests
import urllib.parse


def lookup(symbol):
    """Look up quote for symbol."""
    
    symbol = symbol.lower()
    
    # Temporaryly do a job as api 
    
    if symbol == 'tsla':
        data = {
            'name': 'Tesla Inc',
            'price': 196.89,
        }
        return data
    elif symbol == 'aapl':
        data = {
            'name': 'Apple Inc',
            'price': 151.01,
        }
        return data
    elif symbol == 'tsla':
        data = {
            'name': 'Amazon.com, Inc',
            'price': 97.61,
        }
        return data
    elif symbol == 'tsla':
        data = {
            'name': 'Microsoft Corp',
            'price': 263.10,
        }
        return data
    else:
        return None

    

    # # Contact API
    
    # try:
    #     api_key = os.environ.get("API_KEY")
    #     url = f"http://api.marketstack.com/v1/eod?access_key=771d0d6d57415ad504b8ffdc7d980575&symbols={symbol}"
    #     response = requests.get(url)
    #     response.raise_for_status()
    # except requests.RequestException:
    #     return None

    # # Parse response
    # try:
    #     quote = response.json()
    #     return {
    #         "name": quote["companyName"],
    #         "price": float(quote["latestPrice"]),
    #         "symbol": quote["symbol"]
    #     }
    # except (KeyError, TypeError, ValueError):
    #     return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
