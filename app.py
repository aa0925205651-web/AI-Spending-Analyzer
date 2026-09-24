from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(page_title="消費分析", page_icon="📊")
st.title("消費分析")
st.write("上傳 CSV 消費紀錄，查看總金額與各類別的支出。")

uploaded_file = st.file_uploader("上傳 CSV（需要 category、amount 欄位）", type="csv")
csv_file = uploaded_file if uploaded_file is not None else Path(__file__).with_name("spending.csv")

try:
    spending = pd.read_csv(csv_file)
except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeDecodeError, OSError):
    st.error("無法讀取 CSV，請確認檔案格式正確。")
    st.stop()

if not {"category", "amount"}.issubset(spending.columns):
    st.error("CSV 必須包含 category 和 amount 欄位。")
    st.stop()

if spending.empty:
    st.warning("CSV 沒有消費紀錄。")
    st.stop()

spending["amount"] = pd.to_numeric(spending["amount"], errors="coerce")
if spending["amount"].isna().any() or spending["category"].isna().any():
    st.error("每筆紀錄都需要有效的 category 和數字 amount。")
    st.stop()

if uploaded_file is None:
    st.info("目前顯示 spending.csv 範例資料。")

total = spending["amount"].sum()
largest = spending.loc[spending["amount"].idxmax()]
by_category = spending.groupby("category", as_index=False)["amount"].sum()

col1, col2 = st.columns(2)
col1.metric("總消費金額", f"{total:,.2f}")
col2.metric("最大單筆消費", f"{largest['amount']:,.2f}")
st.caption(f"最大單筆消費類別：{largest['category']}")

st.subheader("各類別消費總金額")
st.dataframe(by_category, hide_index=True, width="stretch")
st.bar_chart(by_category.set_index("category"))
