# APP 股票與期貨資訊

# Dockerfile
* 本地測試
```docker build -t futures-stock-info .```
```docker run -p 5001:5001 futures-stock-info```

# CICD
* 設定Secrets: 在 GitHub Repository 的 Secrets 設定中，新增 DOCKER_USERNAME 與 DOCKER_PASSWORD。

# 單元測試
```python -m unittest discover tests``` 