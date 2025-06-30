import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('sales.csv')

# Display the first 5 rows
print("Head of the data:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Add a new column for Total Sales
df['Total Sales'] = df['Quantity'] * df['Price']
print("\nData with 'Total Sales' column:")
print(df)

# Group by Region and calculate total sales
sales_by_region = df.groupby('Region')['Total Sales'].sum()
print("\nSales by Region:")
print(sales_by_region.to_string(index=True))  # Clean output

# Group by Product and calculate total sales
sales_by_product = df.groupby('Product')['Total Sales'].sum()
print("\nSales by Product:")
print(sales_by_product.to_string(index=True))  # Clean output

# Plot sales by region
sales_by_region.plot(
    kind='bar',
    title='Total Sales by Region',
    ylabel='Total Sales',
    xlabel='Region',
    color='skyblue'
)
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()

# Plot sales by product
sales_by_product.plot(
    kind='bar',
    title='Total Sales by Product',
    ylabel='Total Sales',
    xlabel='Product',
    color='green'
)
plt.tight_layout()
plt.savefig('sales_by_product.png')
plt.show()