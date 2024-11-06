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
    Welcome to this interactive visualization workshop! Here, you will explore different types of charts 
    and data visualizations using the **Plotly** and **Streamlit** libraries. 
    Let's get started! 🚀
""")

# Add some space for better layout
st.markdown("<br>", unsafe_allow_html=True)


# --- Sidebar: User Input Section ---
st.sidebar.header("👨‍🏫 Enter Your Information")
name = st.sidebar.text_input("Your Name:")
usn = st.sidebar.text_input("Your Roll Number:")
instructor_name = st.sidebar.text_input("Instructor's Name:")

# Display user information if provided
if name and usn and instructor_name:
    st.sidebar.markdown(
        f"**Created by:** {name} (USN: {usn})\n"
        f"**Instructor:** {instructor_name}",
        unsafe_allow_html=True
    )
else:
    st.sidebar.markdown(
        "⚠️ Please fill in the details in the sidebar to personalize the visualization.",
        unsafe_allow_html=True
    )


# --- Dataset Loading Section ---
st.write("## 📊 Dataset Overview")
st.write("This workshop uses the popular **`tips`** dataset, which contains information about restaurant tips.")
st.write("Here is a preview of the data:")

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
    This bar chart displays the **average tip** for each day of the week. The color coding highlights each day uniquely.
    Notice the differences between weekdays and weekends!
""")

# Add a little space for separation
st.markdown("<br>", unsafe_allow_html=True)


# --- Task 2: Additional Interactive Chart ---
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
    This scatter plot shows the relationship between **total bill** and **tip** amounts.
    The points are colored based on whether the meal was during lunch or dinner, giving us insights into customer behavior.
""")

# Add a closing note for engagement
st.markdown("<br><h3 style='text-align: center;'>Thanks for exploring the visualizations! 😊</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Hope you found these interactive visualizations insightful. Happy coding!</p>", unsafe_allow_html=True)
