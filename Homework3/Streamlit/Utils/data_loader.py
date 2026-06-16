import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Homework3\Streamlit\Data\Fact_Transactions.csv",sep = ";")
        return df
    except Exception as error:
        st.error(f"Could not download the data: {error}")


