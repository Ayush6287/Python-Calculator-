import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Sample sales data
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        'Date': pd.date_range('2025-01-01', periods=100, freq='D'),
        'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Watch'], 100),
        'Sales': np.random.randint(1000, 10000, 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
    }
    return pd.DataFrame(data)

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.multiselect("Region", df['Region'].unique(), default=df['Region'].unique())
product = st.sidebar.multiselect("Product", df['Product'].unique(), default=df['Product'].unique())

filtered_df = df[(df['Region'].isin(region)) & (df['Product'].isin(product))]

# Main dashboard
st.title("📊 Sales Performance Dashboard")
st.markdown("---")

# KPIs row
col1, col2, col3, col4 = st.columns(4)
total_sales = filtered_df['Sales'].sum()
avg_sales = filtered_df['Sales'].mean()
total_orders = len(filtered_df)
top_product = filtered_df.groupby('Product')['Sales'].sum().idxmax()

with col1:
    st.metric("Total Sales", f"₹{total_sales:,.0f}", delta="12%")
with col2:
    st.metric("Avg Order Value", f"₹{avg_sales:,.0f}")
with col3:
    st.metric("Total Orders", total_orders)
with col4:
    st.metric("Top Product", top_product)

# Charts row
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig1 = px.bar(region_sales, x='Region', y='Sales', title="Region-wise Sales")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Sales Trend")
    fig2 = px.line(filtered_df, x='Date', y='Sales', title="Daily Sales Trend")
    st.plotly_chart(fig2, use_container_width=True)

# Product performance
st.subheader("Product-wise Performance")
product_sales = filtered_df.groupby('Product')['Sales'].sum().reset_index()
fig3 = px.pie(product_sales, values='Sales', names='Product', title="Sales by Product")
st.plotly_chart(fig3, use_container_width=True)

# Raw data table
with st.expander("View Raw Data"):
    st.dataframe(filtered_df)
