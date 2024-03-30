import pandas as pd
import numpy as np

import seaborn as sns
import streamlit as st

st.title("HR Data Visualization")
st.header("Data isuaization is a powerful tool for human resources (HR) and talent development. By creating clear, interactive, and insightful visual representations, HR can monitor workforce demographics, track employee performance, analyze turnover rates, and identify skill gaps.")

st.info("We will provide you information about data in visualization Form or DataFrame")

st.warning("For any Information please contact with HR Dept")
data = pd.read_csv("hrdata1.csv")
##data.head(1)
st.success("File is uploaded")

df_cpy_cmp = data.copy()
df_cpy_cmp.head(6)

st.sidebar.title("Welcome to HR")
st.sidebar.image("download.jpg")
# Display the DataFrame using Streamlit
st.write("### Displaying the Dataset")
st.dataframe(df_cpy_cmp)







