import pandas as pd

# Part 1
df = pd.read_csv('datasets/faithful.csv')
print(df.head())
print(df.dtypes)
print(df.shape)

# Part 2
import matplotlib.pyplot as plt

df.plot(kind='scatter', x='eruptions',y='waiting')
plt.show()

# Part 3
from scipy.cluster.vq import kmeans,vq

centroids, distor = kmeans(df,2)
print(centroids,distor)
idx,dist_vector = vq(df,centroids)
# print(idx,dist_vector)

df['Group'] = idx

print(df.head())

# Part 4
plt.scatter(df[df['Group']==1]['eruptions'], df[df['Group']==1]['waiting'], c='b', s=50, alpha=0.5)
plt.scatter(df[df['Group']==0]['eruptions'], df[df['Group']==0]['waiting'], c='g', s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()

# Part 5
print(df.mean())
print(df[df['Group']==1].mean())
print(df[df['Group']==0].mean())