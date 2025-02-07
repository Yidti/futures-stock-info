# Futures Stock Info

這是一個股票資訊的 Web 應用程式，提供最新的股市資料。

## 部署到 Render

這個專案已經部署到 **Render**，你可以透過以下網址來訪問它：

[https://futures-stock-info-latest.onrender.com/](https://futures-stock-info-latest.onrender.com/)

### 自動部署 (CI/CD)

1. **GitHub 連接 Render**  
   Render 自動監聽 GitHub 上的推送（`main` 分支），當程式碼更新時，它會自動觸發重新部署。

2. **Docker 部署**  
   專案使用 Docker 容器進行部署，Render 會讀取專案中的 `Dockerfile`，並根據它來構建並啟動應用程式。

### 手動觸發部署

如果你希望手動觸發部署，請參照以下步驟：

1. 在 GitHub 進行程式碼更新（例如，推送到 `main` 分支）
2. 使用 GitHub Actions 自動推送 Docker 映像到 Docker Hub
3. Render 會自動拉取 Docker 映像並重新部署應用

---

## 防止 Render 進入休眠

Render 的免費計劃會在長時間沒有請求的情況下將應用實例進入休眠狀態，這可能會導致首次請求的延遲。為了避免這種情況，我們可以使用 **[https://cron-job.org/](https://cron-job.org/)** 來定期發送請求，保持應用活躍。

### 設定步驟：
1. 註冊並登錄 **[cron-job.org](https://cron-job.org/)**。
2. 在該網站上創建一個新的任務，設定為定期訪問你的 Render 網站 URL：
   - 設定 URL 為 `https://futures-stock-info-latest.onrender.com/`
   - 設定間隔為每 10 分鐘或你選擇的時間間隔。
   
這樣，**cron-job.org** 會定期訪問你的應用，從而防止它進入休眠狀態。

---


## 開發環境設定

1. 克隆此專案：
    ```bash
    git clone https://github.com/yourusername/futures-stock-info.git
    cd futures-stock-info
    ```

2. 安裝依賴：
    ```bash
    pip install -r requirements.txt
    ```

3. 本地啟動應用：
    ```bash
    python app.py
    ```

---

## 如何貢獻

歡迎提交 pull request 或提出 issue。任何貢獻都非常感謝！

---

## 相關連結

- [Render 部署頁面](https://futures-stock-info-latest.onrender.com/)
- [GitHub Repository](https://github.com/yourusername/futures-stock-info)
