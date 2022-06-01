'''
import pandas as pd
import urllib.request
urllib.request.urlretrieve('http', 'filename.csv')

name_df=pd.read_csv('name.csv')
.info()
.describe()
.columns
.shape

name_df['column_name'] >> pokazuje 1 kolumnę
name_df.column_name >> to samo ale tylko jesli nazwa bez spacji

name_df['column_name'][230]
name_df.at[230, 'column_name']>>>> to samo

name_df[['column_name', 'column_name']] >> wyswietla 2 kolumny

.loc[240]
.head(2)
.tail(20)
.sample(30)
.first_valid_index()
.sum()

'''