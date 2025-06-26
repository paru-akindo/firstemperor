import streamlit as st
import pandas as pd

@st.cache_data
def load_tables():
    csv_url = "https://docs.google.com/spreadsheets/d/…/export?format=csv&gid=236779120"

    # 表1: 1行目をヘッダー、その後30行分（2–31行目）をA–J列で取得
    df1 = pd.read_csv(
        csv_url,
        header=0,        # シート1行目をカラム名に
        skiprows=1,      # 2行目以降を読み始め
        nrows=30,        # 2〜31行目まで
        usecols=range(0,10)
    )

    # 表2: ヘッダー無しで33–35行目のB–C列だけ取得
    df2 = pd.read_csv(
        csv_url,
        header=None,     # カラム名なし
        skiprows=32,     # 33行目から読み始め
        nrows=3,         # 33–35行目
        usecols=[1,2]    # B, C列
    )
    df2.columns = ["商会","合計値"]
    return df1, df2

df1, df2 = load_tables()
st.title("商会別合計 (B33:C35)")
st.dataframe(df2, hide_index=True, use_container_width=True)

st.title("各階層 (A1:J31)")
st.dataframe(df1, use_container_width=True)
