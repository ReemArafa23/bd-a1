import sys
import pandas as pd
import os

df = pd.read_csv(sys.argv[1])

# Insight 1: Average rating per genre
insight1 = df.groupby('genre_main')['avg_rating'].mean().sort_values(ascending=False)
with open("eda-in-1.txt", "w") as f:
    f.write("Average Rating per Genre:\n")
    f.write(insight1.to_string())

# Insight 2: Most-rated movies
insight2 = df.sort_values('rating_count', ascending=False).head(5)[['title', 'rating_count']]
with open("eda-in-2.txt", "w") as f:
    f.write("Top 5 Most Rated Movies:\n")
    f.write(insight2.to_string(index=False))

# Insight 3: Total unique movies
insight3 = df['movieId'].nunique()
with open("eda-in-3.txt", "w") as f:
    f.write(f"Total number of unique movies: {insight3}")

# Call next step
os.system("python3 vis.py res_dpre.csv")
