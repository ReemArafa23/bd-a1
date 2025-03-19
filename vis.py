import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(sys.argv[1])

# Simple visualization: Top 10 most-rated movies
top_movies = df.sort_values('rating_count', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='rating_count', y='title', data=top_movies)
plt.title("Top 10 Most Rated Movies")
plt.xlabel("Number of Ratings")
plt.ylabel("Movie Title")

plt.tight_layout()
plt.savefig("vis.png")

# Call next step
os.system("python3 model.py res_dpre.csv")
