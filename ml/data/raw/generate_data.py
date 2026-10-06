"""Generate sample expense data for training."""
import csv
import random

random.seed(42)

# Realistic expense descriptions mapped to categories
data = [
    # Food
    ("Starbucks latte", "food"),
    ("Pizza Hut dinner", "food"),
    ("Grocery store", "food"),
    ("Restaurant lunch", "food"),
    ("KFC bucket", "food"),
    ("Bakery bread", "food"),
    ("Coffee shop", "food"),
    ("Sushi takeout", "food"),
    ("Burger King meal", "food"),
    ("Fresh vegetables market", "food"),

    # Transport
    ("Uber ride", "transport"),
    ("Bus ticket", "transport"),
    ("Taxi to airport", "transport"),
    ("Petrol refill", "transport"),
    ("Train ticket", "transport"),
    ("Metro pass", "transport"),
    ("Parking fee", "transport"),
    ("Bike rental", "transport"),
    ("CNG fare", "transport"),
    ("Rickshaw ride", "transport"),

    # Utilities
    ("Electricity bill", "utilities"),
    ("Water bill", "utilities"),
    ("Internet bill", "utilities"),
    ("Gas bill", "utilities"),
    ("Mobile recharge", "utilities"),
    ("Cable TV", "utilities"),
    ("Phone bill", "utilities"),
    ("Broadband payment", "utilities"),

    # Shopping
    ("Amazon order", "shopping"),
    ("Clothes shopping", "shopping"),
    ("Books purchase", "shopping"),
    ("Electronics store", "shopping"),
    ("Shoe purchase", "shopping"),
    ("Furniture mall", "shopping"),
    ("Gift shop", "shopping"),
    ("Online shopping", "shopping"),
    ("New headphones", "shopping"),
    ("Laptop accessories", "shopping"),
]

with open("sample_expenses.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["description", "category"])
    writer.writerows(data)

print(f"Wrote {len(data)} rows to sample_expenses.csv")