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

major_ticks_x = np.arange(150, 1150, 50)
minor_ticks_x = np.arange(150, 1150, 10)
major_ticks_y = np.arange(0, 75000, 5000)
minor_ticks_y = np.arange(0, 75000, 1000)

ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Scope [ADC Counts]')

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x, minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y, minor=True)

ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')

ax.set_xlim(150, 1000)
ax.set_ylim(0, 70000)
plt.margins(0)

plt.show()