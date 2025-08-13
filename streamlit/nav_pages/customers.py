import streamlit as st
import plotly.express as px
import sys
from pathlib import Path
# Add etl_process to path
sys.path.append(str(Path(__file__).parent.parent.parent / "etl_process" / "src"))
from transform.customers_by_country import get_customer_by_city_and_country

df = get_customer_by_city_and_country()

def show_customers():
    st.header("Customer Insights")
    
# Summary statistics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cities", len(df))

with col2:
    st.metric("Total Countries", len(df['country'].unique()))

with col3:
    st.metric("Total Customers", df['total_customers'].sum())

# Country analysis
customers_by_country = df.groupby('country', as_index=False)['total_customers'].sum().sort_values(ascending=False, by='total_customers')
fig_country = px.bar(customers_by_country, x='total_customers', y='country',
                     title="Total Customers by Country",
                     color='total_customers')
fig_country.update_layout(
    height=1000,
    width=700
)
st.plotly_chart(fig_country)