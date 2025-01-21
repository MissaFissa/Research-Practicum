import matplotlib.pyplot as plt 
import click
from research_practicum.data_gathering import DataGathering, Path, pd, np

plt.rcParams.update({'font.size': 8})

@click.command()
@click.argument('figs')
def plot_tests(figs):

    filename_400 = 'data_400mu_csv/12_measurements_400mu'
    filename_200 = 'data_200mu_csv/12_measurements_200mu'
    filename = (f'{filename_400},{filename_200}')
    data = DataGathering(filename)
    # data.gather_data()

    fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 75000, 5000)
    minor_ticks_y = np.arange(0, 75000, 1000)

    axs1[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))
    axs1[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))

    for i in range(len(data.dict_400)):

        axs1[0].plot(data.wavelengths, data.df_400[data.dict_400[i]], label=f'{data.dict_400[i]}')
        axs1[1].plot(data.wavelengths, data.df_200[data.dict_200[i]], label=f'{data.dict_200[i]}')

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

    fig2, axs2 = plt.subplots(2, 2, figsize=(14, 8), facecolor='whitesmoke')
    fig2.set_label('fig2')

    axs2[0,0].plot(data.wavelengths_400nm, data.n_eff_400_15deg, c='dodgerblue', ls='dotted')
    axs2[0,1].plot(data.wavelengths_400nm, data.n_eff_200_15deg, c='dodgerblue', ls='dotted')
    axs2[1,0].plot(data.wavelengths_400nm, data.n_eff_400_0deg, c='dodgerblue', ls='dotted')
    axs2[1,1].plot(data.wavelengths_400nm, data.n_eff_200_0deg, c='dodgerblue', ls='dotted')

    major_ticks_x_2 = np.arange(400, 950, 50)
    minor_ticks_x_2 = np.arange(400, 950, 10)
    major_ticks_y_2_400 = np.arange(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)) + 0.5, 0.5)
    minor_ticks_y_2_400 = np.arange(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)) + 0.5, 0.1)
    major_ticks_y_2_200 = np.arange(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)) + 0.5, 0.5)
    minor_ticks_y_2_200 = np.arange(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)) + 0.5, 0.1)

    # axs2[0,0].set_yticks(major_ticks_y_2_400)
    # axs2[0,0].set_yticks(minor_ticks_y_2_400, minor=True)
    # axs2[0,1].set_yticks(major_ticks_y_2_200)
    # axs2[0,1].set_yticks(minor_ticks_y_2_200, minor=True)
    # axs2[0,0].set_ylim(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)))
    # axs2[0,1].set_ylim(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)))

    for ax in axs2.flatten():

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Calculated effectice index')

        ax.set_xticks(major_ticks_x_2)
        ax.set_xticks(minor_ticks_x_2, minor=True)

        ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_facecolor('dimgrey')

        axs2[0,0].title.set_text('$15\\degree$ $400\\mu$')
        axs2[0,1].title.set_text('$15\\degree$ $200\\mu$')
        axs2[1,0].title.set_text('$0\\degree$ $400\\mu$')
        axs2[1,1].title.set_text('$0\\degree$ $200\\mu$')

    fig2.suptitle(f' {filename} ', fontsize=20)
    plt.tight_layout()
    plt.margins(0)

    for i in figs:

        plt.close('fig'+i)
    
    plt.show()

@click.command()
@click.argument('figs')
def plot_bellyfat(figs):

    filename = 'data_experiment/bellyfat'
    data = DataGathering(filename)

    fig1, axs1 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 75000, 5000)
    minor_ticks_y = np.arange(0, 75000, 1000)

    axs1[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))
    axs1[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))

    for i in range(len(data.dict_400)):

        axs1[0].plot(data.wavelengths, data.df_400[data.dict_400[i]], label=f'{data.dict_400[i]}')
        axs1[1].plot(data.wavelengths, data.df_200[data.dict_200[i]], label=f'{data.dict_200[i]}')

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
    fig2.set_label('fig2')

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
    
    axs2[0].title.set_text('$15\\degree$ $400\\mu$')
    axs2[1].title.set_text('$15\\degree$ $200\\mu$')

    plt.tight_layout()
    plt.margins(0)
    fig2.suptitle(f' {filename} ', fontsize=20)

    for i in figs:

        plt.close('fig'+i)
    
    plt.show()

@click.command()
@click.argument('figs')
def plot_calibration(figs):

    filename = 'data_experiment/calibration'

    data = DataGathering(filename)

    fig1, axs1 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 75000, 5000)
    minor_ticks_y = np.arange(0, 75000, 1000)

    axs1[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))
    axs1[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))

    for i in range(len(data.dict_400)):

        axs1[0].plot(data.wavelengths, data.df_400[data.dict_400[i]], label=f'{data.dict_400[i]}')
        axs1[1].plot(data.wavelengths, data.df_200[data.dict_200[i]], label=f'{data.dict_200[i]}')

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
    fig1.suptitle(f' {filename} ', fontsize=20)
    plt.tight_layout()
    plt.margins(0)

    fig2, axs2 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig2.set_label('fig2')

    major_ticks_x_2 = np.arange(400, 1150, 50)
    minor_ticks_x_2 = np.arange(400, 1150, 10)
    major_ticks_y_2 = np.arange(0, 75000, 5000)
    minor_ticks_y_2 = np.arange(0, 75000, 1000)

    axs2[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 6)))
    axs2[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 6)))

    for i in range(len(data.scaled_400)):

        axs2[0].plot(data.wavelengths_400nm, data.scaled_400[i], label = f'{data.good_400[i]}')
        axs2[1].plot(data.wavelengths_400nm, data.scaled_200[i], label = f'{data.good_200[i]}')

    for ax in axs2.flatten():

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Scope [ADC Counts]')
        ax.set_xticks(major_ticks_x_2)
        ax.set_xticks(minor_ticks_x_2, minor=True)
        ax.set_yticks(major_ticks_y_2)
        ax.set_yticks(minor_ticks_y_2, minor=True)
        ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
        ax.set_xlim(400, 1100)
        ax.set_ylim(0, 70000)
        ax.legend(loc='upper left', prop={'size': 8})
        ax.set_facecolor('dimgrey')

    fig2.suptitle(f' {filename} ', fontsize=20)
    plt.tight_layout()
    plt.margins(0)

    fig3, axs3 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig3.set_label('fig3')

    axs3[0].plot(data.wavelengths_400nm, data.n_eff_400_15deg, c='dodgerblue', ls='dotted')
    axs3[1].plot(data.wavelengths_400nm, data.n_eff_200_15deg, c='dodgerblue', ls='dotted')

    major_ticks_x_3 = np.arange(400, 950, 50)
    minor_ticks_x_3 = np.arange(400, 950, 10)
    major_ticks_y_3_400 = np.arange(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)) + 0.5, 0.5)
    minor_ticks_y_3_400 = np.arange(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)) + 0.5, 0.1)
    major_ticks_y_3_200 = np.arange(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)) + 0.5, 0.5)
    minor_ticks_y_3_200 = np.arange(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)) + 0.5, 0.1)

    axs3[0].set_yticks(major_ticks_y_3_400)
    axs3[0].set_yticks(minor_ticks_y_3_400, minor=True)
    axs3[1].set_yticks(major_ticks_y_3_200)
    axs3[1].set_yticks(minor_ticks_y_3_200, minor=True)
    axs3[0].set_ylim(int(min(data.n_eff_400_15deg)), int(max(data.n_eff_400_15deg)))
    axs3[1].set_ylim(int(min(data.n_eff_200_15deg)), int(max(data.n_eff_200_15deg)))

    for ax in axs3:

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Calculated effectice index')

        ax.set_xticks(major_ticks_x_3)
        ax.set_xticks(minor_ticks_x_3, minor=True)

        ax.grid(which='major', alpha=0.5, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.3, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_facecolor('dimgrey')

        axs3[0].title.set_text('$15\\degree$ $400\\mu$')
        axs3[1].title.set_text('$15\\degree$ $200\\mu$')

    fig3.suptitle(f' {filename} ', fontsize=20)
    plt.tight_layout()
    plt.margins(0)

    fig4, axs4 = plt.subplots(1, figsize=(14, 8), facecolor='whitesmoke')
    fig4.set_label('fig4')

    axs4.plot(data.wavelengths_400nm, data.water_indices, c='dodgerblue', ls='dotted')

    major_ticks_x_4 = np.arange(400, 950, 50)
    minor_ticks_x_4 = np.arange(400, 950, 10)
    major_ticks_y_4 = np.arange(round(min(data.water_indices),2), round(max(data.water_indices),2) + 0.005, 0.005)
    minor_ticks_y_4 = np.arange(round(min(data.water_indices),2), round(max(data.water_indices),2) + 0.005, 0.001)

    axs4.set_xticks(major_ticks_x_4)
    axs4.set_xticks(minor_ticks_x_4, minor=True)
    axs4.set_yticks(major_ticks_y_4)
    axs4.set_yticks(minor_ticks_y_4, minor=True)
    axs4.grid(which='major', alpha=0.5, lw=.8, ls='--')
    axs4.grid(which='minor', alpha=0.3, lw=.6, ls='--')
    axs4.set_xlim(400, 900)
    axs4.set_ylim(min(data.water_indices), max(data.water_indices))
    axs4.set_xlabel('Wavelength [nm]')
    axs4.set_ylabel('Refractive index')
    axs4.set_facecolor('dimgrey')
    fig4.suptitle(f' Water indices ', fontsize=20)

    plt.tight_layout()
    plt.margins(0) 

    for i in figs:

        plt.close('fig'+i)
    
    plt.show()