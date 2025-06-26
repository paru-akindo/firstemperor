import streamlit as st
import pandas as pd

@st.cache_data
def load_all():
    sheet_id = "<SPREADSHEET_ID>"
    gid      = "0"
    csv_url  = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTFOIQtAvilcjBplaklTqvDLg5KAYA8jkU9wL8pBEnQurFp9m62Z4rqbTGWPar0Y4keCqYSjm5qTM2t/pub?gid=236779120&single=true&output=csv"
    return pd.read_csv(csv_url)

df_all = load_all()

# ① A1:J31 (0始まりの iloc で [0:31)×[0:10) を切り出し)
df1 = df_all.iloc[0:31, 0:10]

# — 表2: B33:C35 —（0-indexベースで行32–34, 列1–2）
df2 = df_all.iloc[32:35, 1:3].reset_index(drop=True)

st.title("商会別合計")
st.dataframe(df2, hide_index=True, use_container_width=True)

st.title("各階層")
st.dataframe(df1)


