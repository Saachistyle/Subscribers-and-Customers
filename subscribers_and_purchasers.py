import pandas as pd
import os
from datetime import datetime, timedelta

# Ensure Outputs folder exists
output_dir = "Outputs"
os.makedirs(output_dir, exist_ok=True)

# Load datasets
mailing_list = pd.read_csv('Klaviyo Main List.csv')
orders_data = pd.read_csv('Shopify Orders.csv')
customers_ai = pd.read_csv('Customers AI List.csv')

# Normalize email columns
mailing_list['Email'] = mailing_list['Email'].str.lower()
orders_data['Email'] = orders_data['Email'].str.lower()
customers_ai['EMAIL'] = customers_ai['EMAIL'].str.lower()

# Define date references
today = datetime.now()
thirty_days_ago = today - timedelta(days=30)
sixty_days_ago = today - timedelta(days=60)

# Convert dates to datetime objects
customers_ai['last_active'] = pd.to_datetime(customers_ai['last_active'], errors='coerce').dt.tz_convert(None)
orders_data['Created at'] = pd.to_datetime(orders_data['Created at'], errors='coerce').apply(lambda x: x.tz_localize(None) if pd.notnull(x) else x)

# Task 1: Purchased but not subscribed
purchased_not_subscribed = orders_data[~orders_data['Email'].isin(mailing_list['Email'])]
purchased_not_subscribed.to_csv(f'{output_dir}/Purchased2024_Not_Subscribed.csv', index=False)

# Task 2: Subscribed but not purchased
subscribed_not_purchased = mailing_list[~mailing_list['Email'].isin(orders_data['Email'])]
subscribed_not_purchased.to_csv(f'{output_dir}/Subscribed_Not_Purchased2024.csv', index=False)

# Task 3: Purchased, not subscribed, and used discounts other than WELCOME20
discount_users = purchased_not_subscribed[
    (purchased_not_subscribed['Discount Code'].notna()) & 
    (purchased_not_subscribed['Discount Code'] != 'WELCOME20')
]
discount_users.to_csv(f'{output_dir}/Purchased_2024Not_Subscribed_With_Discount.csv', index=False)

# Task 4: Subscribed, never purchased, but active in the last 30 days
active_subscribed = subscribed_not_purchased[
    subscribed_not_purchased['Email'].isin(
        customers_ai[customers_ai['last_active'] >= thirty_days_ago]['EMAIL']
    )
]
active_subscribed.to_csv(f'{output_dir}/Subscribed_Active_Last_30_Days.csv', index=False)

# Task 5: Customers not purchased in the last 60 days, active in the last 30 days, excluding Task 4
no_purchase_last_60_days = orders_data[orders_data['Created at'] >= sixty_days_ago]
inactive_purchasers = customers_ai[
    (~customers_ai['EMAIL'].isin(no_purchase_last_60_days['Email'])) &
    (customers_ai['last_active'] >= thirty_days_ago) &
    (~customers_ai['EMAIL'].isin(active_subscribed['Email']))
]
inactive_purchasers.to_csv(f'{output_dir}/Inactive_Customers_Active_Last_30_Days.csv', index=False)

print("CSV files created and stored in the 'Outputs' folder:")
print(f"{output_dir}/Purchased2024_Not_Subscribed.csv")
print(f"{output_dir}/Subscribed_Not_Purchased2024.csv")
print(f"{output_dir}/Purchased_2024Not_Subscribed_With_Discount.csv")
print(f"{output_dir}/Subscribed_Active_Last_30_Days.csv")
print(f"{output_dir}/Inactive_Customers_Active_Last_30_Days.csv")
