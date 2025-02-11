import matplotlib.pyplot as plt 
import numpy as np
from test_data_gathering import DataTests, DataExperiment

data = DataTests()
data.background_correction()
data.scale()
data.sellmeier()
data.effective_index()

experiment = DataExperiment()
experiment.background_correction()
experiment.scale()

plt.rcParams.update({'font.size': 8})

fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8), facecolor='whitesmoke')

major_ticks_x = np.arange(150, 1150, 50)
minor_ticks_x = np.arange(150, 1150, 10)
major_ticks_y = np.arange(0, 75000, 5000)
minor_ticks_y = np.arange(0, 75000, 1000)

axs1[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))
axs1[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))

for i in range(1,13):

    axs1[0].plot(data.df_400[data.dict_400[0]], data.df_400[data.dict_400[i]], label=f'{data.dict_400[i]}')
    axs1[1].plot(data.df_200[data.dict_200[0]], data.df_200[data.dict_200[i]], label=f'{data.dict_200[i]}')

for ax in axs1:

    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Scope [ADC Counts]')
    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)
    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)
    ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
    ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
    ax.set_xlim(150, 1100)
    ax.set_ylim(0, 70000)
    ax.legend(prop={'size': 8})
    ax.set_facecolor('dimgrey')

axs1[0].set_title('400$\\mu$ fiber')
axs1[1].set_title('200$\\mu$ fiber')

plt.tight_layout()
plt.margins(0)

fig2, axs2 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')

axs2[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 6)))
axs2[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 6)))

for i in range(len(data.scaled_400)):

    axs2[0].plot(data.wavelengths_400nm, data.scaled_400[i], label = f'{data.good_400[i]}')
    axs2[1].plot(data.wavelengths_400nm, data.scaled_200[i], label = f'{data.good_200[i]}')

for ax in axs2.flatten():

    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Scope [ADC Counts]')
    ax.set_xticks(major_ticks_x)
    ax.set_xticks(minor_ticks_x, minor=True)
    ax.set_yticks(major_ticks_y)
    ax.set_yticks(minor_ticks_y, minor=True)
    ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
    ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
    ax.set_xlim(150, 1100)
    ax.set_ylim(0, 70000)
    ax.legend(loc='upper left', prop={'size': 8})
    ax.set_facecolor('dimgrey')

plt.tight_layout()
plt.margins(0)

fig3, axs3 = plt.subplots(2, 2, figsize=(14, 8), facecolor='whitesmoke')

axs3[0,0].plot(data.wavelengths_400nm, data.n_eff_400_15deg, c='dodgerblue', ls='dotted')
axs3[0,1].plot(data.wavelengths_400nm, data.n_eff_400_0deg, c='dodgerblue', ls='dotted')

axs3[1,0].plot(data.wavelengths_400nm, data.n_eff_200_15deg, c='dodgerblue', ls='dotted')
axs3[1,1].plot(data.wavelengths_400nm, data.n_eff_200_0deg, c='dodgerblue', ls='dotted')

major_ticks_x_3 = np.arange(400, 950, 50)
minor_ticks_x_3 = np.arange(400, 950, 10)
# major_ticks_y_3 = np.arange(0, 75000, 5000)
# minor_ticks_y_3 = np.arange(0, 75000, 1000)

for ax in axs3.flatten():

    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Calculated effectice index')

    ax.set_xticks(major_ticks_x_3)
    ax.set_xticks(minor_ticks_x_3, minor=True)
    # ax.set_yticks(major_ticks_y_3)
    # ax.set_yticks(minor_ticks_y_3, minor=True)

    ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
    ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
    ax.set_xlim(400, 900)
    # ax.set_ylim(0, 70000)
    ax.set_facecolor('dimgrey')

axs3[0,0].title.set_text('$15\\degree$ $400\\mu$')
axs3[0,1].title.set_text('$0\\degree$ $400\\mu$')
axs3[1,0].title.set_text('$15\\degree$ $200\\mu$')
axs3[1,1].title.set_text('$0\\degree$ $200\\mu$')

fig3.suptitle(' Test Measurements ', fontsize=20)
plt.tight_layout()
plt.margins(0)

fig4, axs4 = plt.subplots(1, figsize=(12, 8), facecolor='whitesmoke')

axs4.plot(data.wavelengths_400nm, data.water_indices, c='dodgerblue')

major_ticks_x_4 = np.arange(400, 950, 50)
minor_ticks_x_4 = np.arange(400, 950, 10)
major_ticks_y_4 = np.arange(1.3, 1.4, 0.005)
minor_ticks_y_4 = np.arange(1.3, 1.4, 0.001)

axs4.set_xticks(major_ticks_x_4)
axs4.set_xticks(minor_ticks_x_4, minor=True)
axs4.set_yticks(major_ticks_y_4)
axs4.set_yticks(minor_ticks_y_4, minor=True)
axs4.grid(which='major', alpha=0.5, lw=.8, ls='--')
axs4.grid(which='minor', alpha=0.3, lw=.6, ls='--')
axs4.set_xlim(400, 900)
axs4.set_xlabel('Wavelength [nm]')
axs4.set_ylabel('Refractive index')
axs4.set_facecolor('dimgrey')

plt.tight_layout()
plt.margins(0)

fig5, axs5 = plt.subplots(2, 2, figsize=(14, 8), facecolor='whitesmoke')

axs5[0,0].plot(experiment.wavelengths_400nm, experiment.scaled_400_experiment[0], c='dodgerblue')
axs5[0,1].plot(experiment.wavelengths_400nm, experiment.scaled_400_experiment[1], c='dodgerblue')

axs5[1,0].plot(experiment.wavelengths_400nm, experiment.scaled_400_experiment[2], c='dodgerblue')
axs5[1,1].plot(experiment.wavelengths_400nm, experiment.scaled_400_experiment[3], c='dodgerblue')

major_ticks_x_5 = np.arange(400, 950, 50)
minor_ticks_x_5 = np.arange(400, 950, 10)
major_ticks_y_5 = np.arange(0, 75000, 5000)
minor_ticks_y_5 = np.arange(0, 75000, 1000)

for ax in axs5.flatten():

    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Scope [ADC Counts]')

    ax.set_xticks(major_ticks_x_5)
    ax.set_xticks(minor_ticks_x_5, minor=True)
    # ax.set_yticks(major_ticks_y_5)
    # ax.set_yticks(minor_ticks_y_5, minor=True)

    ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
    ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
    ax.set_xlim(400, 900)
    # ax.set_ylim(0, 70000)
    ax.set_facecolor('dimgrey')

axs5[0,0].title.set_text('Fat tissue $15\\degree$ $400\\mu$')
axs5[0,1].title.set_text('Muscle tissue $15\\degree$ $400\\mu$')
axs5[1,0].title.set_text('Red muscle tissue $15\\degree$ $200\\mu$')
axs5[1,1].title.set_text('Skin tissue $15\\degree$ $200\\mu$')

fig5.suptitle(' Experiment Measurements ', fontsize=20)
plt.tight_layout()
plt.margins(0)

# plt.close(fig1)
plt.close(fig2)
plt.close(fig3)
plt.close(fig4)
plt.close(fig5)

plt.show()