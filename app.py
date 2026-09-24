import pandas as pd

data = {
    "category": ["Food", "Transport", "Entertainment", "Food", "Shopping"],
    "amount": [120, 50, 300, 180, 1200]
}

df = pd.DataFrame(data)

print("=== AI Spending Analyzer ===")

print("\nYour spending records:")
print(df)

print("\nTotal spending:")
print(df["amount"].sum())

print("\nSpending by category:")
print(df.groupby("category")["amount"].sum())

largest = df.loc[df["amount"].idxmax()]

print("\nLargest expense:")
print(f"{largest['category']}: ${largest['amount']}")
