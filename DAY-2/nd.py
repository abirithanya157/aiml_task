import pandas as pd

df = pd.read_csv("data2.csv")

print("Original Data")
print(df)

df["salary_normalization"] = (
    (df["salary"] - df["salary"].min()) /
    (df["salary"].max() - df["salary"].min())
)

print("\nNormalized Data:")
print(df)