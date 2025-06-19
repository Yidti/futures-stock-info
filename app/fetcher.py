import yfinance as yf
import time
import os
import json

# --- 快取設定 ---
CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)
CACHE_DURATION = 60  # 快取有效時間（秒）

def _get_from_cache(key):
    cache_file = os.path.join(CACHE_DIR, f"{key}.json")
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            try:
                data = json.load(f)
                timestamp = data.get("timestamp", 0)
                if time.time() - timestamp < CACHE_DURATION:
                    return data.get("payload")
            except json.JSONDecodeError:
                return None
    return None

def _set_to_cache(key, payload):
    cache_file = os.path.join(CACHE_DIR, f"{key}.json")
    data = {
        "timestamp": time.time(),
        "payload": payload
    }
    with open(cache_file, 'w') as f:
        json.dump(data, f)

def fetch_stock_data(symbol):
    """使用 yfinance 取得個股報價資料。"""
    cached_data = _get_from_cache(f"stock_{symbol}")
    if cached_data:
        return cached_data

    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="5m")
        if not data.empty:
            latest_data = data.iloc[-1]
            result = {
                "Open": latest_data["Open"],
                "High": latest_data["High"],
                "Low": latest_data["Low"],
                "Close": latest_data["Close"],
                "Volume": latest_data["Volume"]
            }
            _set_to_cache(f"stock_{symbol}", result)
            return result
        return None
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None

def fetch_futures_data(symbol):
    """使用 yfinance 取得期貨資料。"""
    cached_data = _get_from_cache(f"futures_{symbol}")
    if cached_data:
        return cached_data

    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1d")
        if not data.empty:
            latest_data = data.iloc[-1]
            result = {
                "Open": latest_data["Open"],
                "High": latest_data["High"],
                "Low": latest_data["Low"],
                "Close": latest_data["Close"],
                "Volume": latest_data["Volume"]
            }
            _set_to_cache(f"futures_{symbol}", result)
            return result
        return None
    except Exception as e:
        print(f"Error fetching futures data for {symbol}: {e}")
        return None

if __name__ == "__main__":
    print(fetch_stock_data("TSLA"))
    print(fetch_futures_data("ES=F"))
