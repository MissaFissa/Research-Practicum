import pandas as pd
from pathlib import Path

cwd = Path.cwd()

df_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
info_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
dict_400 = dict(enumerate(df_400))

df_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
info_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
dict_200 = dict(enumerate(df_200))

x = []
for i in range(1,13):
    x.append()
print(df_400)