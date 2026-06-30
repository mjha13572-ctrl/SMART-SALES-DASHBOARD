import streamlit as st
import pandas as pd
import plotly.express as px
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from datetime import datetime
from backend.file_extractor import load_file

def generate_pdf(total_sales, total_profit, total_orders,
                  best_category, recommendations):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    current_time = datetime.now().strftime("%d %B %Y | %I:%M %p")


    story.append(Paragraph("<b><font size =20>SMART SALES DASHBOARD REPORT</font></b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(
    Paragraph(
        f"<b>Generated On:</b> {current_time}",
        styles["Normal"]
    )
)

    story.append(
    Paragraph("<b><font size=16>Executive Summary</font></b>",
              styles["Heading1"])
)
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"Total Sales: ₹{total_sales:,.2f}", styles["Normal"]))
    story.append(Paragraph(f"Total Profit: ₹{total_profit:,.2f}", styles["Normal"]))
    story.append(Paragraph(f"Total Orders: {total_orders}", styles["Normal"]))
    story.append(Paragraph(f"Best Category: {best_category}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<br/><b><font size =16>Business Recommendations</font></b>", styles["Heading1"]))

    for rec in recommendations:
        story.append(Paragraph(f"✓ {rec}", styles["Normal"]))

    doc.build(story)

    buffer.seek(0)

    return buffer



st.set_page_config(
    page_title="Smart Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Smart Sales Dashboard")
uploaded_file = st.file_uploader(
    "📂 Upload your sales CSV file",
    type=["csv", "xlsx", "xls", "pdf", "docx"]
)

if uploaded_file is not None:
    df = load_file(uploaded_file)
    st.sidebar.success("Using uploaded dataset")
else:
    df = pd.read_csv("sample_data/sales.csv")
    st.sidebar.info("Using default dataset: sales.csv")

required_columns = [
    "Order_ID",
    "Order_Date",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Total_Sales",
    "Payment_Method",
    "Customer_Type",
    "Profit"
]
missing_columns = [
    col for col in required_columns
    if col not in df.columns
]
if missing_columns:
    st.error(
        f"❌ Invalid dataset!\n\nMissing columns: {', '.join(missing_columns)}"
    )
    st.stop()

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
total_profit = filtered_df["Profit"].sum()
profit_margin = (total_profit / total_sales) * 100

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"₹{total_sales:,.2f}")

with col2:
    st.metric("🛒 Total Orders", total_orders)

with col3:
    st.metric("📈 Average Sale", f"₹{average_sales:,.2f}")

with col4:
    st.metric("💹 Total Profit", f"₹{total_profit:,.2f}", delta=f"{profit_margin:.1f}% margin")


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

profit_region = (
    filtered_df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
)
profit_fig = px.bar(
    profit_region, x="Region",
    y="Profit",
    color="Region",
    title="💹 Profit by Region",
    color_discrete_sequence=px.colors.qualitative.Pastel)


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

st.subheader("🤖 Smart Business Recommendations")
recommendations = []
# Lowest Performing Region
region_sales = df.groupby("Region")["Total_Sales"].sum()
lowest_region = region_sales.idxmin()

recommendations.append(
    f"📍 Focus on the **{lowest_region}** region to improve sales through targeted marketing."
)

# Best Customer Type
customer_sales = df.groupby("Customer_Type")["Total_Sales"].sum()
best_customer = customer_sales.idxmax()

recommendations.append(
    f"👥 **{best_customer}** customers generate the highest revenue. Consider loyalty rewards."
)

# Most Profitable Category
category_profit = df.groupby("Category")["Profit"].sum()
best_category = category_profit.idxmax()

recommendations.append(
    f"🏆 **{best_category}** is the most profitable category. Increase inventory and promotions."
)

# Profit Margin
profit_margin = (df["Profit"].sum() / df["Total_Sales"].sum()) * 100

if profit_margin < 20:
    recommendations.append(
        f"📉 Profit margin is only **{profit_margin:.1f}%**. Review pricing and supplier costs."
    )
elif profit_margin < 35:
    recommendations.append(
        f"⚠️ Profit margin is **{profit_margin:.1f}%**. There is room for improvement."
    )
else:
    recommendations.append(
        f"📈 Excellent profit margin of **{profit_margin:.1f}%**. Maintain your current strategy."
    )

# Payment Method
top_payment = df["Payment_Method"].mode()[0]

recommendations.append(
    f"💳 Most customers prefer **{top_payment}**. Ensure this payment option remains fast and reliable."
)

#display all the insights
for recommendation in recommendations:
    st.markdown(f"- {recommendation}")

pdf = generate_pdf(
    total_sales,
    total_profit,
    total_orders,
    best_category,
    recommendations
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

col7, = st.columns(1)    

with col7:
    st.subheader("Region wise profit")
    st.plotly_chart(profit_fig, use_container_width=True )    

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.sidebar.download_button(
    label="📄 Download PDF Report",
    data=pdf.getvalue(),
    file_name="sales_report.pdf",
    mime="application/pdf"
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