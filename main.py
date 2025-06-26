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

# ② A33:C35 は 33行目→0始まりでインデックス32、終了は35→インデックス35(排他)まで。
#    また列は A→0、C→2 なので [32:35, 0:3)
df2 = df_all.iloc[32:35, 0:3]

st.title("表1: A1:J31")
st.dataframe(df1)

st.title("表2: A33:C35")
st.dataframe(df2)
