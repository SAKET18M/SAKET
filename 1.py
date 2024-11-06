# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")

# Add some space for aesthetics
st.markdown("<br>", unsafe_allow_html=True)

# --- Input for Author Information ---
st.sidebar.header("Interactive Visualization Workshop - Plotly")

# Collect author details from the sidebar input
name = st.sidebar.text_input("Enter your name:")
usn = st.sidebar.text_input("Enter your roll number:")
instructor_name = st.sidebar.text_input("Instructor's name:")

# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: teal;'>Created by:</h5>"
        f"<p style='color: white;'>Name: {name} (USN: {usn})</p>"
        f"<p style='color: white;'>Instructor: {instructor_name}</p>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<p style='color: gray;'>Please fill in the details in the sidebar.</p>", 
        unsafe_allow_html=True
    )

# --- Load Dataset ---
st.write("## Dataset Overview")
st.write("The dataset used for visualizations is the `tips` dataset, which contains information about restaurant tips.")

# Load the 'tips' dataset from Seaborn
tips = sns.load_dataset('tips')

# Display the first few rows of the dataset
st.write(tips.head())

# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")

# Create the bar chart with Plotly
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)

# Display the chart in Streamlit
st.plotly_chart(fig2)

# Add a closing note
st.markdown("<br><p style='color: gray;'>Hope you found this visualization workshop helpful!</p>", unsafe_allow_html=True)
