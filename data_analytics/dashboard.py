import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data.csv", sep=";", decimal=".")

df["date"] = pd.to_datetime(df["date"], dayfirst=True)

df = df.sort_values("date")
df["month"] = df["date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Month", df["month"].unique())

df_filtered = df[df["month"] == month]

df_filtered

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtered, x="date", y="total", title="Expenses per date")
col1.plotly_chart(fig_date, use_container_width=True)

type_total = df_filtered.groupby("type")[["total"]].sum().reset_index()
fig_type = px.bar(type_total, x="type", y="total", title="Expenses per type")
col2.plotly_chart(fig_type, use_container_width=True)

fig_type_pie = px.pie(df_filtered, values="total", names="type", title="Expenses per type")
col3.plotly_chart(fig_type_pie, use_container_width=True)