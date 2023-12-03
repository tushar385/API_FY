# print from datbase

import sqlite3
import pandas as pd
s='eqt1'
conn=sqlite3.connect("realtime.db")
data=pd.read_sql_query(f"SELECT * FROM {s}", conn)
conn.close()
print(data)


# to represent ohlc data

data.rename(columns = {'ts':'date'}, inplace = True)
data = data.set_index(['date'])
data.index = pd.to_datetime(data.index)
ticks = data.loc[:, ['price']]
ohlcv_dict = {'volume': 'last'}
A=data['volume'].resample('1T').agg(ohlcv_dict)
df=ticks['price'].resample('1min').ohlc().dropna()
print(df)


# cli command - python retrivedatabase.py