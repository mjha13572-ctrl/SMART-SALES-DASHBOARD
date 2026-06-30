import pandas as pd
import matplotlib.pyplot as plt

def generate_product_sales_chart():
    df = pd.read_csv("sample_data/sales.csv")

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        product_sales.index,
        product_sales.values,
        color="skyblue"
    )

    plt.title("Total Sales by Product")
    plt.xlabel("Products")
    plt.ylabel("Total Sales (₹)")
    plt.xticks(rotation=45)

    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{int(bar.get_height())}",
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.tight_layout()
    plt.savefig("assets/total_sales_by_product.png")
    plt.close()


if __name__ == "__main__":
    generate_product_sales_chart()