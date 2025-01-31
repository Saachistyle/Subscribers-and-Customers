File Download Instructions:
    1. Download The Shopify Orders to compare against and name "Shopify Orders"
    2. Download the Klaviyo Main List and name "Klaviyo Main List"
    3. Download Customers AI most update list and name "Customers AI List"

Current data:
    - Shopify: 2024 Orders
    - Klaviyo: Downloaded 12/20/24
    - Customers.ai: Downloaded 12/23/24


How To Run:
    - run subscibers_and_purchasers.py in chosen environment


Outputs:
    - Purchased2024_Not_Subscribed.csv: Customers who made a purchase in 2024 but are not subscribed to the email list.
    - Subscribed_Not_Purchased2024.csv: Customers who are subscribed to the email list but have not made a purchase in 2024.
    - Purchased_2024Not_Subscribed_With_Discount.csv: Customers who made a purchase in 2024, are not subscribed, and used a discount code other than "WELCOME20".
    - Subscribed_Active_Last_30_Days.csv: Customers who are subscribed, have never purchased, but were active in the last 30 days.
    - Inactive_Customers_Active_Last_30_Days.csv: Customers who have not purchased in the last 60 days, but were active in the last 30 days.
        - Excludes customers already listed in Subscribed_Active_Last_30_Days.csv.