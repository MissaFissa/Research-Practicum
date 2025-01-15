import matplotlib.pyplot as plt 
import numpy as np
from data_gathering import DataGathering
import analysis

data = DataGathering()
data.scale()
data.background_correction()
data.effective_index()


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

fig6, axs6 = plt.subplots(2, 2, figsize=(10, 8))

for i in range(len(data.scaled_400_light)):

    axs6[0,0].plot(analysis.wavelengths, data.scaled_400_light[i])
    axs6[0,1].plot(analysis.wavelengths, data.scaled_200_light[i])

    axs6[1,0].plot(analysis.wavelengths, data.unscaled_400_light[i], label = f'{i+1}')
    axs6[1,1].plot(analysis.wavelengths, data.unscaled_200_light[i])
    print(data.scaled_400_light[i])
fig6.legend()

fig7, axs7 = plt.subplots(2, 2, figsize=(10, 8))

axs7[0,0].plot(data.wavelengths_400nm, data.n_eff_positive_400)
axs7[0,1].plot(data.wavelengths_400nm, data.n_eff_negative_400)

axs7[1,0].plot(data.wavelengths_400nm, data.n_eff_positive_200)
axs7[1,1].plot(data.wavelengths_400nm, data.n_eff_negative_200)

axs7[0,0].title.set_text('$+n_{eff}$  $400\\mu$')
axs7[0,1].title.set_text('$-n_{eff}$  $400\\mu$')
axs7[1,0].title.set_text('$+n_{eff}$  $200\\mu$')
axs7[1,1].title.set_text('$-n_{eff}$  $200\\mu$')

plt.setp(axs7[0,0], xlim=(400,1100), ylim=(-3,3))
plt.setp(axs7[0,1], xlim=(400,1100))
plt.setp(axs7[1,0], xlim=(400,1100))
plt.setp(axs7[1,1], xlim=(400,1100))

plt.tight_layout()
# plt.setp(axs7, xlim=(400,1100), ylim=(-3,3))

plt.close(fig1)
plt.close(fig2)
plt.close(fig3)
plt.close(fig4)
plt.close(fig5)
plt.close(fig6)
# plt.close(fig7)

plt.show()