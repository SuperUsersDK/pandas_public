import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/books.txt',sep='\t')
df.fillna(0, inplace=True)
print(df)

group = df.groupby(['alder','periode'])
print(group.size())
print(group.sum())
group.sum().plot(kind='barh',stacked=True)
plt.show()