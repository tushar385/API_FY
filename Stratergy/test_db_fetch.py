# print from datbase

import sqlite3
import pandas as pd
s='RSI'
conn=sqlite3.connect("Stratergy.db")
data=pd.read_sql_query(f"SELECT * FROM {s}", conn)
conn.close()
print(data.tail())
# print('0:', data['close'])
print('2:',data['close'].iloc[-1])


