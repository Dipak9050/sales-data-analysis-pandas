import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales_data.csv")

# View first 5 rows
print(df.head())

# Basic info
print(df.info())

# Total sales by product
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)

# Plot bar chart
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Filter high sales
high_sales = df[df["Sales"] > 1000]
print(high_sales)

# Check shape
print("Shape of dataset:", df.shape)
