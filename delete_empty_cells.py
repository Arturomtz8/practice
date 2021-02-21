import pandas as pd

data = pd.read_excel('eros.xlsx')
data.to_csv('data.csv') # encoding="latin_1", low_memory=False
# data.dropna(subset=['CECO', 'TIENDA'], inplace=True) # "url del producto", "title"
data.drop_duplicates(subset=['tienda'], keep=False, inplace=True) # "title", "url del producto"

data.to_excel("eros_final.xlsx", encoding="utf_8_sig", index=False)
