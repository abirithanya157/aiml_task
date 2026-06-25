import pandas as pd

# Read dataset
df = pd.read_csv("data.csv")

# Show missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing names with "Unknown"
df["name"] = df["name"].fillna("Unknown")

# Fill missing roll numbers with "Not Available"
df["rollno"] = df["rollno"].fillna("Not Available")

# Fill missing marks with average marks
df["marks"] = df["marks"].fillna(df["marks"].mean())

# Display preprocessed data
print("\nPreprocessed Data:")
print(df)