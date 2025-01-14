import matplotlib.pyplot as plt 
import numpy as np
import data
import analysis

fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8))

for i in range(1,13):

    axs1[0].plot(data.df_400[data.dict_400[0]], data.df_400[data.dict_400[i]], label=f'{i}')
    axs1[1].plot(data.df_200[data.dict_200[0]], data.df_200[data.dict_200[i]], label=f'{i}')

major_ticks_x = np.arange(150, 1150, 50)
minor_ticks_x = np.arange(150, 1150, 10)
major_ticks_y = np.arange(0, 75000, 5000)
minor_ticks_y = np.arange(0, 75000, 1000)

for ax in axs1:

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

axs1[0].set_title('400$\\mu$ fiber')
axs1[1].set_title('200$\\mu$ fiber')

plt.tight_layout()
plt.margins(0)

fig2, axs2 = plt.subplots(2, 2, figsize=(10, 8))

axs2[0,0].plot(analysis.wavelengths, analysis.R_IL_400_0deg)
axs2[0,1].plot(analysis.wavelengths, analysis.IL_400_6ms_0deg)

axs2[1,0].plot(analysis.wavelengths, analysis.R_IL_200_0deg)
axs2[1,1].plot(analysis.wavelengths, analysis.IL_200_5ms_0deg)

plt.setp(axs2[0,0], xlim=(400,1100), ylim=(0,0.3))
plt.setp(axs2[1,0], xlim=(400,1100), ylim=(0,0.3))




fig3, axs3 = plt.subplots(2, 2, figsize=(10, 8))

axs3[0,0].plot(analysis.wavelengths, analysis.R_IL_400_0deg_water)
axs3[0,1].plot(analysis.wavelengths, analysis.R_IL_400_15deg_water)

axs3[1,0].plot(analysis.wavelengths, analysis.R_IL_400_15deg_water)
axs3[1,1].plot(analysis.wavelengths, analysis.R_IL_200_15deg_water)

plt.setp(axs3, xlim=(400,1100), ylim=(0,0.3))

fig4 = plt.figure()
gs = fig4.add_gridspec(2, 2, hspace=0, wspace=0)
axs4 = gs.subplots(sharex=True, sharey=True)

axs4[0,0].plot(analysis.wavelengths, analysis.R_IL_400_0deg_water)
axs4[0,1].plot(analysis.wavelengths, analysis.cor_R_IL_400_0deg_water)

# axs4[0,1].plot(analysis.wavelengths, analysis.R_IL_400_15deg_water)

axs4[1,0].plot(analysis.wavelengths, analysis.R_IL_400_15deg_water)
axs4[1,1].plot(analysis.wavelengths, analysis.R_IL_200_15deg_water)

# plt.setp(axs4, xlim=(400,1100), ylim=(0,0.3))

fig5, axs5 = plt.subplots(2, 2, figsize=(10, 8))

axs5[0,0].plot(analysis.wavelengths, analysis.fresnel_400_6ms_0deg)
axs5[0,1].plot(analysis.wavelengths, analysis.IL_400_6ms_0deg)

axs5[1,0].plot(analysis.wavelengths, analysis.fresnel_200_5ms_0deg)
axs5[1,1].plot(analysis.wavelengths, analysis.IL_200_5ms_0deg)

# plt.close(fig1)
plt.close(fig2)
plt.close(fig3)
plt.close(fig4)
# plt.close(fig5)

plt.show()