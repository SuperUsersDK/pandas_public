import pandas as pd

# Part 1
df = pd.read_csv('datasets/temperatur.csv')
print(df.head())
print(df.dtypes)


# Part 2
df['Max'] = df.max(axis=1)

# Part 3
df['Min'] = df.min(axis=1)

print(df.head())

# Part 4
df['Max_Min_Diff'] = df['Max']-df['Min']

rowid = df['Max_Min_Diff'].idxmax()
print(df.iloc[rowid])

# Part 5
rowid = df['Max_Min_Diff'].idxmin()
print(df.iloc[rowid])

# Part 6
rowids = df.groupby('Continent')['Max_Min_Diff'].idxmax()
print(rowids)

# Part 7
rowids = df.groupby('Continent')['Max_Min_Diff'].idxmin()
print(rowids)
