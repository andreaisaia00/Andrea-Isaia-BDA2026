from Utils.data_loader import load_data
from Utils.data_manipulation import tot_t, top5_sector, top3, top5_industry
from Utils.utils import clean_spines
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# Setting the main aspect of the page.
st.set_page_config(page_title="Time Analysis",layout="centered")

df = load_data()

st.title("Time Analysis")
st.write("Choose a start date and an ending date")

# Creating the time interval.
col_start, col_end = st.columns(2)
start_date = col_start.date_input("Start date", value=pd.to_datetime("2024-01-01"))
end_date = col_end.date_input("End date", value=pd.to_datetime("2024-12-31"))

st.divider()

if start_date >= end_date:
    st.error("The start date must be before the end date.")
else:
    st.subheader("Total number of transactions in the choosen period")
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    st.line_chart(tot_t(start,end,df))

st.divider()

# Top 3 traded symbols by transaction count barchart.
st.subheader("Top 3 traded symbols by transaction count")
df_top3 = top3(start,end,df)

# Creating th chart with matplotlib
fig1, ax1 = plt.subplots(figsize=(10,6))

ax1.barh(df_top3.index,df_top3["n_transactions"])
ax1.set_xlabel("Number of transactions")
ax1.set_ylabel("Simbol")
clean_spines(ax1)
ax1.grid(axis="x",alpha=0.25)

st.pyplot(fig1)

st.divider()

# Top 5 sectors by transaction count barchart.
st.subheader("Top 5 sectors by transaction count")
df_top5_sector = top5_sector(start,end,df)

# Creating th chart with matplotlib
fig2, ax2 = plt.subplots(figsize=(10,6))

ax2.barh(df_top5_sector.index,df_top5_sector["n_transactions"])
ax2.set_xlabel("Number of transactions")
ax2.set_ylabel("Sector")
clean_spines(ax2)
ax2.grid(axis="x",alpha=0.25)

st.pyplot(fig2)

st.divider()


# Top 5 industries by transaction count barchart.
st.subheader("Top 5 industries by transaction count")
df_top5_industry = top5_industry(start,end,df)

# Creating th chart with matplotlib
fig3, ax3 = plt.subplots(figsize=(10,6))

ax3.barh(df_top5_industry.index,df_top5_industry["n_transactions"])
ax3.set_xlabel("Number of transactions")
ax3.set_ylabel("Industry")
clean_spines(ax3)
ax3.grid(axis="x",alpha=0.25)

st.pyplot(fig3)
