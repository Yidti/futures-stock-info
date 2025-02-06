FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔與程式碼
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 設定環境變數（若有需要，例如 API_KEY）
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# 對外開放的 port
EXPOSE 5001

# 啟動應用
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
