# APP 股票與期貨資訊

## 簡介
本專案提供即時股票與期貨資訊，並透過 Docker 進行容器化部署，同時整合 CI/CD 來自動化測試與部署流程。

---

## 🚀 本地開發與測試
### **Docker 環境建置與運行**
1. **建置 Docker Image**
   ```sh
   docker build -t futures-stock-info .
   ```
2. **運行容器**
   ```sh
   docker run -p 5001:5001 futures-stock-info
   ```
---

## 部署到 Render

這個專案已經部署到 **Render**，你可以透過以下網址來訪問它：

[https://futures-stock-info-latest.onrender.com/](https://futures-stock-info-latest.onrender.com/)

---

## 🔄 CI/CD 自動化流程
本專案使用 GitHub Actions 進行 CI/CD，當推送 (`push`) 或合併 (`pull_request`) 至 `main` 分支時，會自動執行：
1. **安裝相依套件**
2. **執行單元測試**
3. **建置 Docker Image**
4. **將 Image 推送至 Docker Hub**
5. **Render會依照Docker Hub自動部署**

註：若只修改文件內容而無其他程式碼更動（例如修改 README.md），則不會觸發 CI/CD 流程。
### **GitHub Secrets 設定**
在 GitHub Repository **Settings > Secrets** 中新增以下憑證：
- `DOCKER_USERNAME`：Docker Hub 帳號
- `DOCKER_PASSWORD`：Docker Hub 密碼

---

## 📦 部署與 Docker Hub 更新
當 CI/CD 成功執行後，最新版本的 Docker Image 會自動推送至 Docker Hub。

🔗 [Docker Hub - `futures-stock-info`](https://hub.docker.com/repository/docker/rekam/futures-stock-info/)

若需手動更新至 Docker Hub，請執行：
```sh
docker login -u <DOCKER_USERNAME> -p <DOCKER_PASSWORD>
docker tag futures-stock-info rekam/futures-stock-info:latest
docker push rekam/futures-stock-info:latest
```

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

## 🛠 單元測試
專案內建單元測試，請執行以下指令來驗證功能：
```sh
python -m unittest discover tests
```

## 相關連結

- [Render 部署頁面](https://futures-stock-info-latest.onrender.com/)
- [GitHub Repository](https://github.com/yourusername/futures-stock-info)

