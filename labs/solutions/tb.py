import pandas as pd

# Part 1
df = pd.read_csv('datasets/tb.csv')
print(df['year'].unique())
print(df.describe())
# Part 2
df = df.rename(columns={'iso2':'country'})

#Part 3
df.columns = df.columns.str.lstrip('new_sp_')
print(df.columns)
print(df.head())

#Part 4
df.drop(['','m04','m514','f04','f514'],axis=1,inplace=True)
print(df.head())
#Dunno hvorfor de ikke betyder noget

#Part5
#The columns _country_ and year

#Part 6
df = pd.melt(df, id_vars=['year', 'country'])
print(df.shape) # (92304, 4)

#Part 7
df['sex'] = df['variable'].str[0]

#Part 8
df['variable'] = df['variable'].str[1:]

