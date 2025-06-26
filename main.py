import streamlit as st
import pandas as pd

@st.cache_data
def load_sheet():
    csv_url = (
      "https://docs.google.com/spreadsheets/d/e/"
      "2PACX-1vTFOIQtAvilcjBplaklTqvDLg5KAYA8jkU9wL8pBEnQurFp9m62Z4rqbTGWPar0Y4keCqYSjm5qTM2t"
      "/pub?gid=236779120&single=true&output=csv"
    )
    # header=0 で1行目をカラムに、自動で型推定
    return pd.read_csv(csv_url, header=0)

df_all = load_sheet()

# —— 表1: A1:J31 —— (0始まりなので行0–30, 列0–9)
df1 = df_all.iloc[0:31, 0:10]

# —— 表2: B33:C35 —— (行32–34, 列1–2)
df2 = (
    df_all
    .iloc[32:35, 1:3]           # B33:C35 を抽出
    .reset_index(drop=True)     # 元の行番号を消して 0,1,2… に
)
df2.columns = ["商会", "合計値"]  # 任意のカラム名に

st.title("商会別合計 (B33:C35)")
st.dataframe(df2, hide_index=True, use_container_width=True)

st.title("各階層 (A1:J31)")
st.dataframe(df1, use_container_width=True)
