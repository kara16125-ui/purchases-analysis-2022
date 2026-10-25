import pandas as pd
import matplotlib.pyplot as plt

path = r"D:\LEARN BROGRAMMING ALL\archive (1)\Compras2022.xlsx"
df = pd.read_excel(path)

# Q1: Top 5 suppliers by total spent
by_supplier = (
    df.groupby("proveedor")["total_siniva"].sum().sort_values(ascending=False).head(5)
)
print(by_supplier)

by_supplier.plot(kind="barh")
plt.title("Top 5 suppliers by total purchases")
plt.xlabel("Total (before VAT)")
plt.tight_layout()
plt.show()

# Q2: Purchases by month
df["month"] = df["fecha"].dt.month
by_month = df.groupby("month")["total_siniva"].sum()
print(by_month)

by_month.plot(kind="line", marker="o")
plt.title("Total purchases by month (2022)")
plt.xlabel("Month")
plt.ylabel("Total (before VAT)")
plt.tight_layout()
plt.show()

# Q3: Top 10 products by quantity
by_product = (
    df.groupby("descripcion")["cant"].sum().sort_values(ascending=False).head(10)
)
print(by_product)

by_product.plot(kind="barh")
plt.title("Top 10 products by quantity")
plt.xlabel("Quantity")
plt.tight_layout()
plt.show()