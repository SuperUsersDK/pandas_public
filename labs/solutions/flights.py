import pandas as pd
import matplotlib.pyplot as plt

def convert():
    pass

# Part 1
df = pd.read_csv('datasets/flights.csv'
                    , parse_dates={'Date':["Year","Month","DayofMonth"]}
                    , dtype={'UniqueCarrier':'category','Origin':'category','Dest':'category','DepTime':'str', 'ArrTime':'str','FlightNum':'str'})
df['DayOfWeek'] -= 1

print(df.head())

print(df.dtypes)
print(df.shape)

#part 2
print(df[(df['Date'].dt.month==1)&(df['Date'].dt.day==1)].shape)

#Part 3
print(df[(df['UniqueCarrier']=='UA')|(df['UniqueCarrier']=='AA')].shape)

#Part 4
delayed_df = df[(df['DepDelay']>60)]
print(round(delayed_df.shape[0]/df.shape[0]*100,2))

#Part 5
df['Speed'] = df['Distance']/df['AirTime']*60
print(df.head())

# Part 6
avg_delay_per_dest = df.groupby('Dest')['ArrDelay'].mean()
# print(avg_delay_per_dest)

# Part 7
print(avg_delay_per_dest.sort_values()[:6])
avg_delay_per_dest.plot(kind='bar')
# plt.show()

#Part 8
df = df.sort_values(by=['Date'])
counts = df.groupby('Date')['Date'].count().to_frame('FlightCount').reset_index()
df = df.merge(counts, on='Date')
print(df.head())

# Part 9
print(df.sort_values(by=['FlightCount','Date'],ascending=False)[:6])

# Part 10
df['cancel_and_div'] = df['Cancelled']+df['Diverted']
total_cancel_div = df.groupby(['UniqueCarrier'])['cancel_and_div'].sum().to_frame('Number')

dato_fc = df[['Date','FlightCount','UniqueCarrier']].drop_duplicates()

airlines_counts = dato_fc.groupby('UniqueCarrier').sum()

print(airlines_counts)
print(total_cancel_div)
final_df = airlines_counts.merge(total_cancel_div, left_index=True, right_index=True)
final_df['pct'] = final_df['Number']/final_df['FlightCount']*100
print(final_df)