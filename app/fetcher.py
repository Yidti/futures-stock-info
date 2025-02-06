import yfinance as yf

def fetch_stock_data(symbol):
    """
    使用 yfinance 取得個股報價資料。
    這裡使用 period="1d" 與 interval="5m" 來模擬 Alpha Vantage 的 5 分鐘資料，
    若資料不足可以調整 period 與 interval 的參數。
    """
    ticker = yf.Ticker(symbol)
    # 取得當天的 5 分鐘資料，若無資料則可能交易時段外
    data = ticker.history(period="1d", interval="5m")
    if not data.empty:
        latest_data = data.iloc[-1]
        return {
            "Open": latest_data["Open"],
            "High": latest_data["High"],
            "Low": latest_data["Low"],
            "Close": latest_data["Close"],
            "Volume": latest_data["Volume"]
        }
    return None

def fetch_futures_data(symbol):
    """使用 yfinance 取得期貨資料
    例如：S&P 500 E-mini Futures 的符號為 'ES=F'
    """
    ticker = yf.Ticker(symbol)
    # 取得最近一個交易日的資料
    data = ticker.history(period="1d", interval="1d")
    if not data.empty:
        latest_data = data.iloc[-1]
        # 組成一個字典，包含開盤、最高、最低、收盤等資訊
        return {
            "Open": latest_data["Open"],
            "High": latest_data["High"],
            "Low": latest_data["Low"],
            "Close": latest_data["Close"],
            "Volume": latest_data["Volume"]
        }
    return None

if __name__ == "__main__":
    # 簡單測試
    # print(fetch_stock_data("AAPL"))
    print(fetch_stock_data("TSLA"))
    print(fetch_futures_data("ES=F"))
