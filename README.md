# AI Spending Analyzer

一個簡單的 Streamlit 消費分析網頁 App。

## 開始使用

在專案資料夾執行：

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

執行後開啟終端機顯示的網址（通常是 http://localhost:8501）。

上傳 CSV 後，頁面會顯示總消費金額、最大單筆消費、各類別總金額和長條圖。未上傳時會使用 `spending.csv` 範例資料。

CSV 需要 `category` 和 `amount` 兩欄，例如：

```csv
category,amount
Food,120
Transport,50
Food,180
```
