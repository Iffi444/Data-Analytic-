import pandas as pd



import streamlit as st

st.title("HR Data Visualization")
st.header("Data isuaization is a powerful tool for human resources (HR) and talent development. By creating clear, interactive, and insightful visual representations, HR can monitor workforce demographics, track employee performance, analyze turnover rates, and identify skill gaps.")

st.info("We will provide you information about data in visualization Form or DataFrame")

st.warning("For any Information please contact with HR Dept")
data = pd.read_csv("hrdata1.csv")

st.success("File is uploaded")

df_cpy_cmp = data.copy()
df_cpy_cmp.isnull().sum()

#first 5 rows of dataset

st.write("### Displaying the Dataset")
st.write("First 5 Rows of HR DataSet")
st.dataframe(df_cpy_cmp.head())

#Specific 5 columns of dataset

columns_of_interest = ['Employee_Name', 'EmpID', 'Salary', 'Position', 'Sex', 'CitizenDesc','Department']

# Display the first 5 rows of the specified columns
st.write("Specific Columns of HR DataSet")
st.dataframe(df_cpy_cmp[columns_of_interest].head())

st.sidebar.title("Welcome to HR")
st.sidebar.image("download.jpg")
# Display the DataFrame using Streamlit



#how many male and female in HR Department showing with bargraph

gender_counts = df_cpy_cmp.groupby(['State', 'Sex']).size().unstack()

# Plotting bar graph
st.bar_chart(gender_counts)
st.scatter_chart(gender_counts)







