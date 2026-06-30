# 📊 Smart Sales Dashboard

An interactive **Sales Analytics Dashboard** built with **Python, Streamlit, Pandas, Plotly, and ReportLab**. The dashboard enables businesses to analyze sales performance, monitor key performance indicators (KPIs), generate business insights, and export reports with ease.

---

## 🚀 Features

- 📂 Upload sales datasets (CSV & Excel)
- 📄 Basic support for PDF and DOCX file extraction
- 📊 Interactive sales dashboard
- 📈 Dynamic KPI cards
- 🌍 Region-wise sales analysis
- 📦 Product-wise sales analysis
- 📂 Category-wise sales analysis
- 💳 Payment method distribution
- 👥 Customer type distribution
- 📅 Monthly sales trend analysis
- 💹 Region-wise profit analysis
- 🤖 Automated business recommendations based on sales performance
- 📄 Generate downloadable PDF reports
- 📥 Export filtered sales data as CSV
- ✅ Dataset validation with error handling

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **ReportLab**
- **pdfplumber**
- **python-docx**
- **OpenPyXL**

---

## 📂 Project Structure

```text
smart-sales-dashboard/
│
├── assets/
│   └── total_sales_by_product.png
│
├── backend/
│   ├── dataset_analysis.py
│   └── file_extractor.py
│
|── app.py
│
├── reports/
│
├── sample_data/
│   ├── sales.csv
│   ├── sales.test.csv
│   └── wrong.csv
│
├── requirements.txt
├── README.md
├── generate_dataset.py
└── .gitignore
```

---

## 📊 Dashboard Includes

- Sales KPIs
- Product Performance
- Region Performance
- Category Analysis
- Payment Distribution
- Customer Segmentation
- Monthly Sales Trends
- Profit Analysis
- Business Insights
- PDF Report Generation

---

## 📸 Screenshots

### Dashboard

> [dashbord](screenshots/dashboard/dashboard.png)
> [dashbord](screenshots/dashboard/businessinsights.png)
> [dashbord](screenshots/dashboard/downloadpdfreport.png)
> [dashbord](screenshots/dashboard/sidebarsfilters.png)
> [dashbord](screenshots/dashboard/downloadfilterdata.png)


### Charts

> [charts](screenshots/charts/chart1.png)
> [charts](screenshots/charts/chart2.png)
> [charts](screenshots/charts/chart3.png)
> [charts](screenshots/charts/chart4.png)

### Pdf report

> [PDF report](screenshots/PDFreport.png)


---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/mjha13572-ctrl/smart-sales-dashboard.git
```

Move into the project directory

```bash
cd smart-sales-dashboard
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run frontend/app.py
```

---

## 📁 Sample Dataset

A sample sales dataset is available inside the `sample_data` folder.

You can upload your own dataset as long as it contains the required columns:

- Order_ID
- Order_Date
- Product
- Category
- Region
- Quantity
- Total_Sales
- Payment_Method
- Customer_Type
- Profit

---

## 📄 Report Generation

The dashboard can generate a professional PDF report containing:

- Executive Summary
- Total Sales
- Total Profit
- Total Orders
- Best Performing Category
- Smart Business Recommendations

---

## 🔍 Future Improvements

- Sales forecasting using Machine Learning
- Automatic table extraction from PDF files
- Database integration
- User authentication
- Interactive filtering enhancements
- Cloud deployment with database support

---

## 👩‍💻 Author

**Madhuri Jha**

B.Tech Electronics & Communication Engineering  
Aspiring AI & Data Engineer

GitHub: *(https://github.com/mjha13572-ctrl)*

LinkedIn: *(https://www.linkedin.com/in/madhuri-jha-66b076321/)*

---
## 🚀 Live Demo

*(https://your-app-name.streamlit.app)*

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub.

