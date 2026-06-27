import pandas as pd

df = pd.read_csv("data2.csv")

print("Original Data:")
print(df)

# Standardization (Z-score)
df["salary_standardized"] = (
    (df["salary"] - df["salary"].mean()) / df["salary"].std()
)

print("\nStandardized Data:")
print(df)