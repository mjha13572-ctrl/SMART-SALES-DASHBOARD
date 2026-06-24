import csv
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Product details
products = {
    "Laptop": ("Electronics", 55000),
    "Smartphone": ("Electronics", 30000),
    "Tablet": ("Electronics", 20000),
    "Monitor": ("Electronics", 12000),
    "Printer": ("Electronics", 15000),
    "Speaker": ("Accessories", 3500),
    "Headphones": ("Accessories", 2500),
    "Webcam": ("Accessories", 1800),
    "Keyboard": ("Accessories", 1500),
    "Mouse": ("Accessories", 700)
}

regions = ["North", "South", "East", "West"]
customer_types = ["New", "Returning"]
payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]

# Generate a random date between Jan and Jun 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 6, 30)

def random_date():
    days = (end_date - start_date).days
    random_days = random.randint(0, days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Create CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "Order_ID",
        "Order_Date",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Total_Sales",
        "Profit",
        "Region",
        "Customer_Type",
        "Payment_Method"
    ])

    # Generate 200 records
    for order_id in range(1001, 1201):

        product = random.choice(list(products.keys()))
        category, unit_price = products[product]

        quantity = random.randint(1, 5)
        total_sales = quantity * unit_price

        # Profit between 10% and 25%
        profit = round(total_sales * random.uniform(0.10, 0.25), 2)

        writer.writerow([
            order_id,
            random_date(),
            product,
            category,
            quantity,
            unit_price,
            total_sales,
            profit,
            random.choice(regions),
            random.choice(customer_types),
            random.choice(payment_methods)
        ])

print("✅ sales.csv created successfully!")