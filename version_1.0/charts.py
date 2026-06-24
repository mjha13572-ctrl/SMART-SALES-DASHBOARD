import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales.csv")

product_sales = df.groupby("Product")["Total_Sales"].sum()
plt.figure(figsize=(10,6))

bars = plt.bar(
    product_sales.index,
    product_sales.values,
    color="skyblue"
)

plt.title("Total Sales by Product", fontsize=16, fontweight="bold")
plt.xlabel("Products", fontsize=12)
plt.ylabel("Total Sales (₹)", fontsize=12)

plt.xticks(rotation=45)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("total_sales_by_product.png")

plt.show()