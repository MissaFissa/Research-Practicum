import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pathlib import Path

cwd = Path.cwd()
df = pd.read_csv(f'{cwd}/data_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0])
df_dict = dict(enumerate(df))

for value in df_dict.values():
    print(value)