# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.set_page_config(page_title="Interactive Plotly & Streamlit Visualizations", layout="wide")

# Centering the title and adding a short introduction
st.title("✨ Interactive Visualizations with Plotly & Streamlit")
st.markdown("""
    Welcome to this interactive workshop! Here, you'll explore various charts and visualizations using **Plotly** and **Streamlit**. 
    Let's dive into the world of interactive data visualization! 🚀
""")

# Add "Created By" info in the header
st.markdown("<h4 style='text-align: center; color: #2ca02c;'>Created By: SAKET M</h4>", unsafe_allow_html=True)

# Add some space for better layout
st.markdown("<br>", unsafe_allow_html=True)


# --- Dataset Loading Section ---
st.write("## 📊 Dataset Overview")
st.write("""
    In this session, we'll be using the popular **`tips`** dataset, which contains information about tips given in a restaurant setting.
    Below is a preview of the dataset:
""")

# Load Seaborn's tips dataset
tips = sns.load_dataset('tips')

# Display the first few rows of the dataset
st.dataframe(tips.head(), use_container_width=True)

# Add some spacing for aesthetics
st.markdown("<br>", unsafe_allow_html=True)


# --- Task 1: Interactive Bar Chart ---
st.subheader("📝 Task 1: Bar Chart - Average Tip by Day")

# Generate the bar chart using Plotly Express
fig1 = px.bar(
    tips,
    x="day", y="tip", color="day",
    title="💰 Average Tip by Day of the Week",
    labels={"tip": "Average Tip ($)", "day": "Day of the Week"},
    template="plotly_dark",
    color_discrete_map={
        'Thur': '#FF7F0E', 'Fri': '#1F77B4', 'Sat': '#2CA02C', 'Sun': '#D62728'
    }
)

# Display the bar chart in the Streamlit app
st.plotly_chart(fig1, use_container_width=True)

# Add a short note explaining the chart
st.markdown("""
    This bar chart displays the **average tip** given on each day of the week. The color coding helps to distinguish 
    between the days, making it easier to compare tips on weekdays versus weekends.
""")

# Add a little space for separation
st.markdown("<br>", unsafe_allow_html=True)


# --- Task 2: Interactive Scatter Plot ---
st.subheader("📝 Task 2: Scatter Plot - Tip vs. Total Bill")

# Generate a scatter plot to visualize the relationship between `total_bill` and `tip`
fig2 = px.scatter(
    tips,
    x="total_bill", y="tip", color="time",
    title="💡 Tip vs Total Bill (Scatter Plot)",
    labels={"total_bill": "Total Bill ($)", "tip": "Tip ($)", "time": "Time of Day"},
    template="plotly_dark"
)

# Display the scatter plot
st.plotly_chart(fig2, use_container_width=True)

# Short explanation of the chart
st.markdown("""
    This scatter plot shows the relationship between **total bill** and **tip** amounts. The points are colored
    according to the meal time (Lunch or Dinner), providing insights into customer behavior.
""")

# Add some space for separation
st.markdown("<br>", unsafe_allow_html=True)


# --- Closing Message ---
st.markdown("<br><h3 style='text-align: center;'>Thank You for Exploring the Visualizations! 😊</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>We hope you enjoyed these interactive visualizations and gained valuable insights. Happy coding!</p>", unsafe_allow_html=True)
