import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/sale.csv'
                    , parse_dates = True
                    , header=[0,1])
df.columns = ['v1_date','v1_sale','D1','v2_date','v2_sale','D2','v3_date','v3_sale']
df.drop(df.columns[[2,5]],inplace=True, axis=1)
df['v1_date'] = pd.to_datetime(df['v1_date'],format='%d/%m/%Y')
df['v2_date'] = pd.to_datetime(df['v2_date'],format='%d/%m/%Y')
df['v3_date'] = pd.to_datetime(df['v3_date'],format='%d/%m/%Y')

df_v1 = df[['v1_date','v1_sale']]
df_v2 = df[['v2_date','v2_sale']]
df_v3 = df[['v3_date','v3_sale']]

df_v1.set_index('v1_date',inplace=True)
df_v2.set_index('v2_date',inplace=True)
df_v3.set_index('v3_date',inplace=True)

print(df_v1.head())

df_v1_v2 = pd.merge(df_v1,df_v2,how='outer', left_index=True,right_index=True)
df_v1_v2_v3 = pd.merge(df_v1_v2,df_v3,how='outer', left_index=True,right_index=True)
df_v1_v2_v3.dropna(inplace=True, how='all')
df_v1_v2_v3.fillna(0, inplace=True)
print(df_v1_v2_v3)
df_v1_v2_v3.plot(kind='line')
plt.show()


