import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Display the first 5 rows of the specified columnsgit
st.write("Specific Columns of HR DataSet")
st.dataframe(df_cpy_cmp[columns_of_interest].head())

st.sidebar.title("Welcome to HR")
st.sidebar.image("download.jpg")
# Display the DataFrame using Streamlit

gender_counts = df_cpy_cmp.groupby(['Department', 'Sex']).size().unstack()

plt.figure(figsize=(10, 6))  # Set the size of the plot
#sns.barplot(data=gender_counts, palette="husl")  # Create the bar plot
sns.countplot(x="Sex", hue="Sex", data=df_cpy_cmp)
plt.title("Number of Males and Females in Each Department")  # Set the title
plt.xlabel("Sex")  # Set the label for the x-axis
plt.ylabel("Count")  # Set the label for the y-axis
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
st.pyplot(plt)  # Display the plot in Streamlit






