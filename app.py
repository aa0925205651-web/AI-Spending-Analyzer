from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("spending.csv"))

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
