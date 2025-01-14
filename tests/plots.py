import matplotlib.pyplot as plt 
import numpy as np
import data

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

for i in range(1,13):

    axs[0].plot(data.df_400[data.dict_400[0]], data.df_400[data.dict_400[i]], label=f'{i}')
    axs[1].plot(data.df_200[data.dict_200[0]], data.df_200[data.dict_200[i]], label=f'{i}')

major_ticks_x = np.arange(150, 1150, 50)
minor_ticks_x = np.arange(150, 1150, 10)
major_ticks_y = np.arange(0, 75000, 5000)
minor_ticks_y = np.arange(0, 75000, 1000)

for ax in axs:

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
    ax.legend()

axs[0].set_title('400$\\mu$ fiber')
axs[1].set_title('200$\\mu$ fiber')

plt.tight_layout()
plt.margins(0)

plt.show()