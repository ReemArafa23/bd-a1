import sys
import pandas as pd
import os

# Read ratings
ratings = pd.read_csv(sys.argv[1])

# Read movies
movies = pd.read_csv("movies.csv")

# Merge
df = pd.merge(ratings, movies, on='movieId')

# Clean
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Transform: split genres
df['genre_main'] = df['genres'].apply(lambda x: x.split('|')[0] if isinstance(x, str) else 'Unknown')

# Reduce: Average rating and count
agg = df.groupby(['movieId', 'title', 'genre_main']).agg({
    'rating': ['mean', 'count']
}).reset_index()
agg.columns = ['movieId', 'title', 'genre_main', 'avg_rating', 'rating_count']

# Discretize ratings
agg['rating_level'] = pd.cut(agg['avg_rating'],
                             bins=[0, 2.5, 3.5, 5],
                             labels=['Low', 'Medium', 'High'])

# Save result
agg.to_csv('res_dpre.csv', index=False)

# Call next step
os.system("python3 eda.py res_dpre.csv")
