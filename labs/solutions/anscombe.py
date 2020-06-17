import pandas as pd

# Part 1
df = pd.read_csv('datasets/anscombe.csv')

print(df.head())

# Part 2
print(df.describe())
print(df.median())

# Part 3 + 4
import numpy as np

poly1 = np.poly1d(np.polyfit(df['x1'],df['y1'],1))
poly2 = np.poly1d(np.polyfit(df['x2'],df['y2'],1))
poly3 = np.poly1d(np.polyfit(df['x3'],df['y3'],1))
poly4 = np.poly1d(np.polyfit(df['x4'],df['y4'],1))
print(poly1)
print(poly2)
print(poly3)
print(poly4)

# Part 5
import matplotlib.pyplot as plt

ax1 = df.plot(kind='scatter', x='x1', y='y1', color='red') 
ax2 = df.plot(kind='scatter', x='x2', y='y2', color='yellow', ax=ax1)
ax3 = df.plot(kind='scatter', x='x3', y='y3', color='green', ax=ax1)
ax4 = df.plot(kind='scatter', x='x4', y='y4', color='blue', ax=ax1)

plot_x = np.arange(20)

ax5 = plt.plot(plot_x, poly1(plot_x), color='red')
ax6 = plt.plot(plot_x, poly2(plot_x), color='yellow')
ax7 = plt.plot(plot_x, poly3(plot_x), color='green')
ax8 = plt.plot(plot_x, poly4(plot_x), color='blue')

plt.show()