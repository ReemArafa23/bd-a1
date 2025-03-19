# load.py
import sys
import pandas as pd
import os

print("Starting load.py...")

# Read path from argument
input_path = sys.argv[1]
print(f"Reading dataset from: {input_path}")

df = pd.read_csv(input_path)
print("Loaded data, first 5 rows:")
print(df.head())

df.to_csv("res_load.csv", index=False)
print("Saved res_load.csv")

# Call next script (comment this out for now to test load.py alone)
# os.system("python3 dpre.py res_load.csv")

print("load.py finished.")

