import streamlit as st
import pandas as pd

# 公開シートの CSV エクスポートURL (gidは対象シートのID)
sheet_id = "1px1zotoJ5BvWFOfyJetF4YE52hFb99QJP92CjS8OOG4"
gid      = "0"
csv_url  = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTFOIQtAvilcjBplaklTqvDLg5KAYA8jkU9wL8pBEnQurFp9m62Z4rqbTGWPar0Y4keCqYSjm5qTM2t/pub?gid=236779120&single=true&output=csv"

# Pandas で直接読み込む
df = pd.read_csv(csv_url)

st.title("公開スプレッドシートを無料で表示")
st.dataframe(df)
