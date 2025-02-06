from flask import Flask, render_template, jsonify
from fetcher import fetch_stock_data, fetch_futures_data

app = Flask(__name__)

@app.route('/')
def index():
    # 取得一些範例資料
    # stock = fetch_stock_data("AAPL")
    stock = fetch_stock_data("TSLA")
    futures = fetch_futures_data("ES=F")  # 假設 ES=F 是期貨代碼
    return render_template('index.html', stock=stock, futures=futures)

@app.route('/api/refresh')
def refresh_data():
    # 提供一個 API 端點給前端 AJAX 呼叫
    stock = fetch_stock_data("TSLA")
    futures = fetch_futures_data("ES=F")
    return jsonify({'stock': stock, 'futures': futures})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
