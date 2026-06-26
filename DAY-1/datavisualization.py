import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1.csv")
df.columns = df.columns.str.strip()

plt.figure(figsize=(10,8))

# Plot 1 - Bar Chart
plt.subplot(2,2,1)
plt.bar(df["Name"], df["Salary"])
plt.title("Bar Chart")
plt.xlabel("Name")
plt.ylabel("Salary")

# Plot 2 - Line Chart
plt.subplot(2,2,2)
plt.plot(df["Name"], df["Salary"], marker="o")
plt.title("Line Chart")
plt.xlabel("Name")
plt.ylabel("Salary")

# Plot 3 - Scatter Plot
plt.subplot(2,2,3)
plt.scatter(df["Name"], df["Salary"])
plt.title("Scatter Plot")
plt.xlabel("Name")
plt.ylabel("Salary")

# Plot 4 - Pie Chart
plt.subplot(2,2,4)
plt.pie(
    df["Salary"],
    labels=df["Name"],
    autopct="%1.1f%%"
)
plt.title("Pie Chart")
plt.xlabel("Name")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()