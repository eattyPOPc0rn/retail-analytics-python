import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
sales_data = pd.read_csv("product_sales.csv")
marketing_data = pd.read_csv("marketing_campaign.csv")
feedback_data = pd.read_csv("customer_feedback.csv")

# Sidebar filter
st.sidebar.title("Filter")
segment = st.sidebar.selectbox("Choose Customer Segment:", sales_data['Segment'].unique())

# Filtered data
filtered_sales = sales_data[sales_data['Segment'] == segment]
filtered_feedback = feedback_data[feedback_data['Segment'] == segment]

# Dashboard title
st.title("Retail Performance Dashboard")

# Chart 1: Sales by Product
sales_summary = filtered_sales.groupby('Product')['Sales'].sum().reset_index()
fig1 = px.bar(sales_summary, x='Sales', y='Product', orientation='h', title='Total Sales by Product')
st.plotly_chart(fig1)

# Chart 2: Average Satisfaction
avg_satisfaction = filtered_feedback.groupby('Product')['Satisfaction'].mean().reset_index()
fig2 = px.scatter(avg_satisfaction, x='Product', y='Satisfaction', size='Satisfaction',
                  color='Product', title='Avg Customer Satisfaction by Product')
st.plotly_chart(fig2)
