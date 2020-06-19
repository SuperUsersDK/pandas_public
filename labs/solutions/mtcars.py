import pandas as pd

df = pd.read_csv('datasets/mtcars.csv')

print(df.head())

#Shortest way
df.apply(lambda x: print(pd.factorize(x, sort=True) if pd.unique(x).size <= 10 else None), axis=1)


#Shorter way
def find_and_print_less_than_10(x):
    k = pd.unique(x).size
    if k <= 10:
        codes, uniques = pd.factorize(x, sort=True)
        print(codes, uniques)

df.apply(find_and_print_less_than_10,axis=1)

# More manual way.
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


