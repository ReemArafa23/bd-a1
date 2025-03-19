import sys
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1])

# Features for clustering
X = df[['avg_rating', 'rating_count']]

# K-means
kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(X)

# Save cluster counts
counts = df['cluster'].value_counts().sort_index()
with open("k.txt", "w") as f:
    f.write("Records in each cluster:\n")
    f.write(counts.to_string())
