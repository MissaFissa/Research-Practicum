import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pathlib import Path

cwd = Path.cwd()

df = pd.read_csv(f'{cwd}/data_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
df_dict = dict(enumerate(df))

fig, ax = plt.subplots(figsize=(10, 8))

for i in range(1,13):

    ax.plot(df[df_dict[0]], df[df_dict[i]])

ax.grid(True, which = 'minor', lw = .5, alpha = .2)
plt.show()