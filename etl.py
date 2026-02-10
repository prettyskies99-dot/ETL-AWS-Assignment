import pandas as pd

# Extract
data = pd.read_csv("input_data.csv")

# Transform
data["salary"] = data["salary"] * 1.10

# Load
data.to_csv("output_data.csv", index=False)

print("ETL process completed successfully")
