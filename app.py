import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Sales Dashboard")
df = pd.read_csv("sales.csv")

# ---------------- Sidebar Filters ----------------

st.sidebar.header("🔍 Filter Data")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

# Apply Filters
filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Payment_Method"].isin(payment))
]



# ---------------- KPI Section ----------------

total_sales = filtered_df["Total_Sales"].sum()
total_orders = len(filtered_df)
average_sales = filtered_df["Total_Sales"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"₹{total_sales:,.2f}")

with col2:
    st.metric("🛒 Total Orders", total_orders)

with col3:
    st.metric("📈 Average Sale", f"₹{average_sales:,.2f}")


region_sales = filtered_df.groupby("Region")["Total_Sales"].sum().reset_index()

region_fig = px.bar(
    region_sales,
    x="Region",
    y="Total_Sales",
    color="Region",
    title="Total Sales by Region"
)
region_fig.update_layout(showlegend=False)
region_fig.update_layout(height=600)


product_sales = (filtered_df.groupby("Product")["Total_Sales"]
.sum()
.sort_values(ascending=False)
.reset_index()
)

product_fig = px.bar(
    product_sales,
    x="Product",
    y="Total_Sales",
    color="Product",
    title="Product by sales analysis"
)
product_fig.update_layout(showlegend=False)
product_fig.update_layout(height=600)

category_sales = (
    filtered_df.groupby("Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

category_fig= px.bar(
    category_sales,
    x= "Category",
    y= "Total_Sales",
    color="Category",
    title="Category by sales analysis"

)
category_fig.update_layout(showlegend=False)
category_fig.update_layout(height=600)

payment_data = (
    filtered_df.groupby("Payment_Method")
    .size()
    .reset_index(name="Count")
)

payment_fig = px.pie(
    payment_data,
    names="Payment_Method",
    values="Count",
    title="💳 Payment Method Distribution",
    hole=0.4
)



customer_type = (
    filtered_df.groupby("Customer_Type")
    .size()
    .reset_index(name="Count")
)

customer_fig = px.pie(
    customer_type,
    names="Customer_Type",
    values="Count",
    title="Customer type distribution",
    hole=0.4
)


filtered_df["Order_Date"] = pd.to_datetime(filtered_df["Order_Date"])

filtered_df["Month"] = filtered_df["Order_Date"].dt.strftime("%b")

monthly_sales = (
    filtered_df.groupby("Month")["Total_Sales"]
    .sum()
    .reset_index()
)

month_order = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

monthly_sales["Month"] = pd.Categorical(
    monthly_sales["Month"],
    categories=month_order,
    ordered=True
)

monthly_sales = monthly_sales.sort_values("Month")

monthly_sales_fig = px.line(
    monthly_sales,
    x="Month",
    y="Total_Sales",
    title="📈 Monthly Sales Trend",
    markers=True
)


col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Product Sales")
    st.plotly_chart(product_fig, use_container_width=True)

with col2:
    st.subheader("🌍 Region Sales")
    st.plotly_chart(region_fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📂 Category Sales")
    st.plotly_chart(category_fig, use_container_width=True)

with col4:
    st.subheader("💳 Payment Method")
    st.plotly_chart(payment_fig, use_container_width=True) 

col5, col6 = st.columns(2)

with col5:
    st.subheader("👥 Customer Type")
    st.plotly_chart(customer_fig, use_container_width=True)

with col6:
    st.subheader("📈 Monthly Sales Trend")
    st.plotly_chart(monthly_sales_fig, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.markdown("---")
st.subheader("📌 Business Insights")

best_product = filtered_df.groupby("Product")["Total_Sales"].sum().idxmax()
best_region = filtered_df.groupby("Region")["Total_Sales"].sum().idxmax()
best_category = filtered_df.groupby("Category")["Total_Sales"].sum().idxmax()
best_payment = filtered_df["Payment_Method"].mode()[0]
customer_type = filtered_df["Customer_Type"].mode()[0]

st.info(f"""
        
🏆 **Best Selling Product:** {best_product}

🌍 **Best Performing Region:** {best_region}

📂 **Best Category:** {best_category}

💳 **Most Used Payment Method:** {best_payment}

👥 **Majority Customer Type:** {customer_type}

""")
st.dataframe(filtered_df)