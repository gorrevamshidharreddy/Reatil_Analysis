import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Generate Customers

customers = []
for i in range(1, 301):
    customers.append([
        i,
        fake.name(),
        fake.city(),
        fake.date_between(start_date='-2y', end_date='today')
    ])

customers_df = pd.DataFrame(customers, columns=["customer_id", "customer_name", "city", "signup_date"])
customers_df.to_csv("customers.csv", index=False)

# Generate Stores

store_names = ["Hyderabad Central", "Banjara Hills", "Madhapur", "Gachibowli", "Secunderabad"]
stores = []

for i, name in enumerate(store_names, start=1):
    stores.append([i, name, "Hyderabad"])

stores_df = pd.DataFrame(stores, columns=["store_id", "store_name", "city"])
stores_df.to_csv("stores.csv", index=False)

# Generate Categories

category_list = ["Whiskey", "Beer", "Wine", "Vodka", "Rum"]
categories = []

for i, cat in enumerate(category_list, start=1):
    categories.append([i, cat])

categories_df = pd.DataFrame(categories, columns=["category_id", "category_name"])
categories_df.to_csv("categories.csv", index=False)

# Generate Products

products = []
for i in range(1, 101):
    category_id = random.randint(1, 5)
    cost_price = round(random.uniform(200, 1000), 2)
    selling_price = round(cost_price + random.uniform(50, 300), 2)

    products.append([
        i,
        f"Product_{i}",
        category_id,
        cost_price,
        selling_price
    ])

products_df = pd.DataFrame(products, columns=[
    "product_id", "product_name", "category_id",
    "cost_price", "selling_price"
])
products_df.to_csv("products.csv", index=False)

# Generate Sales

sales = []
start_date = datetime(2023, 1, 1)

for i in range(1, 8001):
    sale_date = start_date + timedelta(days=random.randint(0, 600))
    customer_id = random.randint(1, 300)
    store_id = random.randint(1, 5)
    product_id = random.randint(1, 100)
    quantity = random.randint(1, 5)

    sales.append([
        i,
        sale_date.date(),
        customer_id,
        store_id,
        product_id,
        quantity
    ])

sales_df = pd.DataFrame(sales, columns=[
    "sale_id", "sale_date", "customer_id",
    "store_id", "product_id", "quantity"
])
sales_df.to_csv("sales.csv", index=False)

print("Data generation completed successfully!")