import pandas as pd

df = pd.read_csv('datasets/mtcars.csv')

print(df.head())

less_than_10 = []
for i in ['mpg','cyl','hp','drat','wt','qsec','vs','am','gear','carb','name']:
    k = pd.unique(df[i]).size
    if k <= 10:
        less_than_10.append(i)
    print(i, k)

print('Less than 10', len(less_than_10))

for i in less_than_10:
    codes, uniques = pd.factorize(df[i], sort=True)
    print(codes, uniques)


