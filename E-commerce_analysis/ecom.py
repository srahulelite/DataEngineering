# Identify trends, analyze customer segments, and forecast future sales for an online retail business.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("inputs/sales_data_sample.csv", encoding="ISO-8859-1", dtype={'ORDERDATE': 'string'})
df = df[['ORDERNUMBER', 'PRODUCTCODE', 'CUSTOMERID', 'ORDERDATE', 'QUANTITYORDERED', 'PRICEEACH', 'SALES', 'COUNTRY', 'Device']]

# Convert OrderDate to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# # Check for and handle missing values
# df = df.dropna()  # Or fill missing values with appropriate logic

# # Remove duplicates
# df = df.drop_duplicates()

df['ORDERDATE'].fillna(pd.Timestamp('2000-01-01'), inplace=True)


# Extract month and day of week
df['Month'] = df['ORDERDATE'].dt.month
df['DayOfWeek'] = df['ORDERDATE'].dt.dayofweek

# Calculate monthly revenue
monthly_sales = df.groupby('Month').SALES.sum()

# Calculate total spend per customer
customer_lifetime_value = df.groupby('CUSTOMERID').SALES.sum()


# Exploratory Data Analysis (EDA)
# Goal: Identify trends and patterns.
# Questions to answer:
# What are the top-selling products?
# Which days or months are the highest in sales?
# What devices are most orders placed on?

# Top-selling products
top_products = df.groupby('PRODUCTCODE').QUANTITYORDERED.sum().sort_values(ascending=False)
# print(top_products)

# Plotting
top_products.head(10).plot(kind='bar', title='Top 10 Products')
# plt.show()

# Sales by device
device_sales = df.groupby('Device').SALES.sum()
device_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Device Type')
# plt.show()

# Create a customer data subset
customer_data = df.groupby('CUSTOMERID').agg({
    'SALES': 'sum',
    'ORDERNUMBER': 'count',
    'QUANTITYORDERED': 'sum'
}).rename(columns={'SALES': 'TotalSpend', 'ORDERNUMBER': 'OrderFrequency'})

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42).fit(customer_data)
customer_data['Segment'] = kmeans.labels_

# print(customer_data)

from statsmodels.tsa.arima.model import ARIMA

# Aggregate monthly sales
monthly_sales_ts = df.groupby('Month').SALES.sum()

# Build and train ARIMA model
model = ARIMA(monthly_sales_ts, order=(1, 1, 1))
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=1)  # Forecasting next month
print("Next month's sales forecast:", forecast)