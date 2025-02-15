import matplotlib.pyplot as plt 
import click
from research_practicum.data_gathering import DataGathering, np
from research_practicum.analysis import Analysis

plt.rcParams.update({'font.size': 10})

@click.command()
@click.argument('figs', required=False)
def plot_experiment(figs):

    analysis = Analysis()

    fig1, axs1 = plt.subplots(2, 2, figsize=(14, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    axs1[0,0].plot(analysis.wavelengths_400nm, analysis.R_fat_400, c='dodgerblue', ls='dotted', label='$R_{fat}$')
    axs1[0,1].plot(analysis.wavelengths_400nm, analysis.R_muscle_400, c='dodgerblue', ls='dotted', label='$R_{muscle}$')
    axs1[1,0].plot(analysis.wavelengths_400nm, analysis.R_redmuscle_400, c='dodgerblue', ls='dotted', label='$R_{red\\ muscle}$')
    axs1[1,1].plot(analysis.wavelengths_400nm, analysis.R_skin_400, c='dodgerblue', ls='dotted', label='$R_{skin}$')
    axs1[0,0].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_fat_400[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs1[0,1].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_muscle_400[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs1[1,0].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_redmuscle_400[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs1[1,1].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_skin_400[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    
    major_ticks_x_1 = np.arange(400, 950, 50)
    minor_ticks_x_1 = np.arange(400, 950, 10)
    major_ticks_y_1 = np.arange(0, 0.040, 0.005)
    minor_ticks_y_1 = np.arange(0, 0.040, 0.001)

    for ax in axs1.flatten():

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Measured absolute reflectance')
        ax.set_xticks(major_ticks_x_1)
        ax.set_xticks(minor_ticks_x_1, minor=True)
        ax.set_yticks(major_ticks_y_1)
        ax.set_yticks(minor_ticks_y_1, minor=True)
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_ylim(0, 0.035)
        ax.set_facecolor('whitesmoke')
        ax.legend(prop={'size': 10})
        axs1[0,0].title.set_text('Fat $15\\degree$ $400\\mu$')
        axs1[0,1].title.set_text('Muscle $15\\degree$ $400\\mu$')
        axs1[1,0].title.set_text('Red muscle $15\\degree$ $400\\mu$')
        axs1[1,1].title.set_text('Skin $15\\degree$ $400\\mu$')
    
    # fig1.suptitle(' Reflectance of different bellyfat parts ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    fig2, axs2 = plt.subplots(2, 2, figsize=(14, 8), facecolor='whitesmoke')
    fig2.set_label('fig2')

    axs2[0,0].plot(analysis.wavelengths_400nm, analysis.R_fat_200, c='dodgerblue', ls='dotted', label='$R_{fat}$')
    axs2[0,1].plot(analysis.wavelengths_400nm, analysis.R_muscle_200, c='dodgerblue', ls='dotted', label='$R_{muscle}$')
    axs2[1,0].plot(analysis.wavelengths_400nm, analysis.R_redmuscle_200, c='dodgerblue', ls='dotted', label='$R_{red\\ muscle}$')
    axs2[1,1].plot(analysis.wavelengths_400nm, analysis.R_skin_200, c='dodgerblue', ls='dotted', label='$R_{skin}$')
    axs2[0,0].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_fat_200[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs2[0,1].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_muscle_200[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs2[1,0].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_redmuscle_200[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    axs2[1,1].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_skin_200[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    
    major_ticks_x_2 = np.arange(400, 950, 50)
    minor_ticks_x_2 = np.arange(400, 950, 10)
    major_ticks_y_2 = np.arange(0, 0.040, 0.005)
    minor_ticks_y_2 = np.arange(0, 0.040, 0.001)

    for ax in axs2.flatten():

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Measured absolute reflectance')
        ax.set_xticks(major_ticks_x_2)
        ax.set_xticks(minor_ticks_x_2, minor=True)
        ax.set_yticks(major_ticks_y_2)
        ax.set_yticks(minor_ticks_y_2, minor=True)
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_ylim(0, 0.035)
        ax.set_facecolor('whitesmoke')
        ax.legend(prop={'size': 10})

        axs2[0,0].title.set_text('Fat $15\\degree$ $200\\mu$')
        axs2[0,1].title.set_text('Muscle $15\\degree$ $200\\mu$')
        axs2[1,0].title.set_text('Red muscle $15\\degree$ $200\\mu$')
        axs2[1,1].title.set_text('Skin $15\\degree$ $200\\mu$')

    # fig2.suptitle(' Reflectance of different bellyfat parts ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    fig3, axs3 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig3.set_label('fig3')

    axs3[0].plot(analysis.wavelengths_400nm, analysis.R_IL_400, c='dodgerblue', ls='dotted')
    axs3[1].plot(analysis.wavelengths_400nm, analysis.R_IL_200, c='dodgerblue', ls='dotted')

    major_ticks_x_3 = np.arange(400, 950, 50)
    minor_ticks_x_3 = np.arange(400, 950, 10)
    major_ticks_y_3 = np.arange(0, 0.055, 0.01)
    minor_ticks_y_3 = np.arange(0, 0.055, 0.005)

    for ax in axs3:

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Measured absolute reflectance')

        ax.set_xticks(major_ticks_x_3)
        ax.set_xticks(minor_ticks_x_3, minor=True)
        ax.set_yticks(major_ticks_y_3)
        ax.set_yticks(minor_ticks_y_3, minor=True)
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_ylim(0, 0.05)
        ax.set_facecolor('whitesmoke')

    axs3[0].title.set_text('Intralipid $15\\degree$ $400\\mu$')
    axs3[1].title.set_text('Intralipid $15\\degree$ $200\\mu$')

    # fig3.suptitle(' Measured absolute reflectance of Intralipid ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    fig4, axs4 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig4.set_label('fig4')

    axs4[0].set_prop_cycle('color', plt.cm.tab10(np.arange(0, 4, 1)))
    axs4[1].set_prop_cycle('color', plt.cm.tab10(np.arange(0, 4, 1)))

    axs4[0].plot(analysis.wavelengths_400nm, analysis.R_fat_400, ls='dotted', label='$R_{fat}$')
    axs4[0].plot(analysis.wavelengths_400nm, analysis.R_muscle_400, ls='dotted', label='$R_{muscle}$')
    axs4[0].plot(analysis.wavelengths_400nm, analysis.R_redmuscle_400, ls='dotted', label='$R_{red\\ muscle}$')
    axs4[0].plot(analysis.wavelengths_400nm, analysis.R_skin_400, ls='dotted', label='$R_{skin}$')
    
    axs4[1].plot(analysis.wavelengths_400nm, analysis.R_fat_200, ls='dotted', label='$R_{fat}$')
    axs4[1].plot(analysis.wavelengths_400nm, analysis.R_muscle_200, ls='dotted', label='$R_{muscle}$')
    axs4[1].plot(analysis.wavelengths_400nm, analysis.R_redmuscle_200, ls='dotted', label='$R_{red\\ muscle}$')
    axs4[1].plot(analysis.wavelengths_400nm, analysis.R_skin_200, ls='dotted', label='$R_{skin}$')

    # axs4[0].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_muscle_400[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
    # axs4[1].plot(analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], analysis.R_muscle_200[analysis.wavelength_635nm_index], c='red', marker='.', label='635 nm')
   
    major_ticks_x_4 = np.arange(400, 950, 50)
    minor_ticks_x_4 = np.arange(400, 950, 10)
    major_ticks_y_4 = np.arange(0, 0.040, 0.005)
    minor_ticks_y_4 = np.arange(0, 0.040, 0.001)

    for ax in axs4:

        ax.axvline(x=analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], c='black', ls=':', label='635 nm')
        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Measured absolute reflectance')
        ax.set_xticks(major_ticks_x_4)
        ax.set_xticks(minor_ticks_x_4, minor=True)
        ax.set_yticks(major_ticks_y_4)
        ax.set_yticks(minor_ticks_y_4, minor=True)
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_ylim(0, 0.035)
        ax.set_facecolor('whitesmoke')
        ax.legend(prop={'size': 10})

    # axs4[1].axvline(x=analysis.wavelengths_400nm.iloc[analysis.wavelength_635nm_index], c='black', ls=':')

    # fig4.suptitle(' Reflectance of different bellyfat parts ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    fig5, axs5 = plt.subplots(1, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig5.set_label('fig5')

    axs5.plot(analysis.wavelengths_400nm, analysis.R_fat_400, ls='None', label='$R_{fat}$', c='blue', ms=3, marker='d', markevery=10)
    axs5.plot(analysis.wavelengths_400nm, analysis.R_muscle_400, ls='None', label='$R_{muscle}$', c='forestgreen', ms=3, marker='h', markevery=10)
    axs5.plot(analysis.wavelengths_400nm, analysis.R_redmuscle_400, ls='None', label='$R_{red\\ muscle}$', c='red', ms=3, marker='*', markevery=10)
    axs5.plot(analysis.wavelengths_400nm, analysis.R_skin_400, ls='None', label='$R_{skin}$', c='orange', ms=3, marker='+', markevery=10)
        
    major_ticks_x_5 = np.arange(400, 950, 50)
    minor_ticks_x_5 = np.arange(400, 950, 10)
    major_ticks_y_5 = np.arange(0, 0.040, 0.005)
    minor_ticks_y_5 = np.arange(0, 0.040, 0.001)

    ax = axs5

    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Measured absolute reflectance')
    ax.set_xticks(major_ticks_x_5)
    ax.set_xticks(minor_ticks_x_5, minor=True)
    ax.set_yticks(major_ticks_y_5)
    ax.set_yticks(minor_ticks_y_5, minor=True)
    # ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
    # ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    ax.set_xlim(400, 900)
    ax.set_ylim(0, 0.025)
    ax.set_facecolor('whitesmoke')
    ax.legend(prop={'size': 20}, loc='upper center')


    # fig5.suptitle(' Reflectance of different bellyfat parts ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    for i in figs or []:

        plt.close('fig'+i)
    
    plt.show()

@click.command()
@click.argument('figs', required=False)
def plot_tests(figs):

    filename_400 = 'data_400mu_csv/12_measurements_400mu'
    filename_200 = 'data_200mu_csv/12_measurements_200mu'
    filename = (f'{filename_400},{filename_200}')
    data = DataGathering(filename)

    fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 70000, 5000)
    minor_ticks_y = np.arange(0, 70000, 1000)

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
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(150, 1100)
        ax.set_ylim(0, 65000)
        ax.legend(prop={'size': 8})
        ax.set_facecolor('whitesmoke')

    # axs1[0].set_title('400$\\mu$ fiber')
    # axs1[1].set_title('200$\\mu$ fiber')

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
 
    for ax in axs2.flatten():

        ax.set_xlabel('Wavelength [nm]')
        ax.set_ylabel('Calculated effectice index')

        ax.set_xticks(major_ticks_x_2)
        ax.set_xticks(minor_ticks_x_2, minor=True)

        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_facecolor('whitesmoke')

        axs2[0,0].title.set_text('$15\\degree$ $400\\mu$')
        axs2[0,1].title.set_text('$15\\degree$ $200\\mu$')
        axs2[1,0].title.set_text('$0\\degree$ $400\\mu$')
        axs2[1,1].title.set_text('$0\\degree$ $200\\mu$')

    # fig2.suptitle(' Test data ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    # fig3 = plt.figure(figsize=(12, 8), facecolor='whitesmoke')
    # axs3 = fig3.axes
    fig3, axs3 = plt.subplots(figsize=(14, 8), facecolor='whitesmoke')
    fig3.set_label('fig3')

    major_ticks_x_3 = np.arange(400, 1150, 50)
    minor_ticks_x_3 = np.arange(400, 1150, 10)
    major_ticks_y_3 = np.arange(0, 70000, 5000)
    minor_ticks_y_3 = np.arange(0, 70000, 1000)

    # axs3.set_prop_cycle('color', plt.cm.hsv(np.linspace(0, 1, 12)))
    # axs3.set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 12)))

    # axs3.set_prop_cycle('color', plt.cm.tab20(range(12)))

    # for i in range(len(data.dict_400)):

        # axs3.plot(data.wavelengths, data.df_400[data.dict_400[i]], label=f'{data.dict_400[i]}')
        # axs3[1].plot(data.wavelengths, data.df_200[data.dict_200[i]], label=f'{data.dict_200[i]}')

    if ' mu' and ' deg' in data.dict_400[2]:
        
        label2 = data.dict_400[2].replace(' mu', '\u03BC')
        label = label2.replace(' deg', '\u00b0')

    axs3.plot(data.wavelengths, data.df_400[data.dict_400[2]], c='blue', label=f'{label}')

    axs3.set_xlabel('Wavelength [nm]')
    axs3.set_ylabel('Scope [ADC Counts]')
    axs3.set_xticks(major_ticks_x_3)
    axs3.set_xticks(minor_ticks_x_3, minor=True)
    axs3.set_yticks(major_ticks_y_3)
    axs3.set_yticks(minor_ticks_y_3, minor=True)
    axs3.grid(which='major', alpha=0.8, lw=.8, ls='--')
    axs3.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    axs3.set_xlim(400, 1100)
    axs3.set_ylim(0, 65000)
    axs3.legend(prop={'size': 12}, loc='upper left')
    axs3.set_facecolor('whitesmoke')
    # axs3.set_title('400$\\mu$ fiber')

    plt.tight_layout()
    plt.margins(0)

    fig5, axs5 = plt.subplots(1, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig5.set_label('fig2')

    axs5.plot(data.wavelengths_400nm, data.n_eff_400_0deg, c='blue', ls='None', ms=3, marker='x', markevery=5, label='Calulated $n_{eff}$ fiber')

    major_ticks_x_5 = np.arange(400, 950, 50)
    minor_ticks_x_5 = np.arange(400, 950, 10)
    # major_ticks_y_5 = np.arange(400, 950, 50)
    # minor_ticks_y_5 = np.arange(400, 950, 10)

    ax = axs5
    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Calculated effectice index')
    ax.set_xticks(major_ticks_x_5)
    ax.set_xticks(minor_ticks_x_5, minor=True)
    # ax.set_yticks(major_ticks_y_5)
    # ax.set_yticks(minor_ticks_y_5, minor=True)
    # ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
    # ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    ax.legend(prop={'size': 20}, loc='upper center')
    ax.set_xlim(400, 900)
    ax.set_facecolor('whitesmoke')

    # axs5.title.set_text('$15\\degree$ $400\\mu$')

    # fig5.suptitle(' Test data ', fontsize=14)
    plt.tight_layout()
    plt.margins(0)

    for i in figs or []:

        plt.close('fig'+i)
    
    plt.show()

@click.command()
@click.argument('figs', required=False)
def plot_bellyfat(figs):

    filename = 'data_experiment/bellyfat'
    data = DataGathering(filename)

    fig1, axs1 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 70000, 5000)
    minor_ticks_y = np.arange(0, 70000, 1000)

    axs1[0].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 8)))
    axs1[1].set_prop_cycle('color', plt.cm.jet(np.linspace(0, 1, 8)))

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
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(150, 1100)
        ax.set_ylim(0, 65000)
        ax.legend(prop={'size': 8})
        ax.set_facecolor('whitesmoke')

    # axs1[0].set_title('400$\\mu$ fiber')
    # axs1[1].set_title('200$\\mu$ fiber')

    plt.tight_layout()
    plt.margins(0)

    fig2, axs2 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig2.set_label('fig2')

    axs2[0].set_prop_cycle('color', plt.cm.tab10(np.arange(0, 6, 1)))
    axs2[1].set_prop_cycle('color', plt.cm.tab10(np.arange(0, 6, 1)))

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
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(150, 1100)
        ax.set_ylim(0, 65000)
        ax.legend(loc='upper left', prop={'size': 8})
        ax.set_facecolor('whitesmoke')
    
    axs2[0].title.set_text('$15\\degree$ $400\\mu$')
    axs2[1].title.set_text('$15\\degree$ $200\\mu$')
    # fig2.suptitle(f' {filename} ', fontsize=14)

    plt.tight_layout()
    plt.margins(0)

    fig3, axs3 = plt.subplots(1, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig3.set_label('fig3')

    major_ticks_x_3 = np.arange(150, 1150, 50)
    minor_ticks_x_3 = np.arange(150, 1150, 10)
    major_ticks_y_3 = np.arange(0, 70000, 5000)
    minor_ticks_y_3 = np.arange(0, 70000, 1000)

    axs3.set_prop_cycle('color', plt.cm.tab10(np.arange(0, 4, 1)))

    for i in range(len(data.dict_400)):

        if 'dark' not in data.dict_400[i]:

            if '400 mu' and '15 deg' in data.dict_400[i]:
        
                label2 = data.dict_400[i].replace('400 mu', '')
                label = label2.replace('15 deg', '')  
                axs3.plot(data.wavelengths, data.df_400[data.dict_400[i]], label=f'{label}')

    ax = axs3
    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Scope [ADC Counts]')
    ax.set_xticks(major_ticks_x_3)
    ax.set_xticks(minor_ticks_x_3, minor=True)
    ax.set_yticks(major_ticks_y_3)
    ax.set_yticks(minor_ticks_y_3, minor=True)
    # ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
    # ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    ax.set_xlim(400, 1100)
    ax.set_ylim(0, 60000)
    ax.legend(prop={'size': 18})
    ax.set_facecolor('whitesmoke')

    # axs3.set_title('Data gathered from 400$\\mu$ fiber')

    plt.tight_layout()
    plt.margins(0)

    fig4, axs4 = plt.subplots(1, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig4.set_label('fig4')

    major_ticks_x_4 = np.arange(400, 1150, 50)
    minor_ticks_x_4 = np.arange(400, 1150, 10)
    major_ticks_y_4 = np.arange(0, 15000, 2500)
    minor_ticks_y_4 = np.arange(0, 15000, 500)

    axs4.set_prop_cycle('color', plt.cm.tab10(np.arange(0, 4, 1)))

    for i in range(len(data.scaled_400)):

        if 'dark' not in data.scaled_400_dict[i]:

            if '400 mu' and '15 deg' in data.scaled_400_dict[i]:
        
                label2 = data.scaled_400_dict[i].replace('400 mu', '')
                label = label2.replace('15 deg', '')  
                axs4.plot(data.wavelengths_400nm, data.scaled_400[i], label=f'{label}')

    ax = axs4
    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Scope [ADC Counts]')
    ax.set_xticks(major_ticks_x_4)
    ax.set_xticks(minor_ticks_x_4, minor=True)
    ax.set_yticks(major_ticks_y_4)
    ax.set_yticks(minor_ticks_y_4, minor=True)
    # ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
    # ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    ax.set_xlim(400, 1100)
    ax.set_ylim(0, 12500)
    ax.legend(prop={'size': 18})
    ax.set_facecolor('whitesmoke')

    # axs4.set_title('Scaled data gathered from 400$\\mu$ fiber')

    plt.tight_layout()
    plt.margins(0)

    for i in figs or []:

        plt.close('fig'+i)
    
    plt.show()

@click.command()
@click.argument('figs', required=False)
def plot_calibration(figs):

    filename = 'data_experiment/calibration'

    data = DataGathering(filename)

    fig1, axs1 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig1.set_label('fig1')

    major_ticks_x = np.arange(150, 1150, 50)
    minor_ticks_x = np.arange(150, 1150, 10)
    major_ticks_y = np.arange(0, 70000, 5000)
    minor_ticks_y = np.arange(0, 70000, 1000)

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
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(150, 1100)
        ax.set_ylim(0, 65000)
        ax.legend(prop={'size': 8})
        ax.set_facecolor('whitesmoke')

    # axs1[0].set_title('400$\\mu$ fiber')
    # axs1[1].set_title('200$\\mu$ fiber')
    # fig1.suptitle(f' {filename} ', fontsize=20)
    plt.tight_layout()
    plt.margins(0)

    fig2, axs2 = plt.subplots(2, 1, figsize=(14, 8), facecolor='whitesmoke')
    fig2.set_label('fig2')

    major_ticks_x_2 = np.arange(400, 1150, 50)
    minor_ticks_x_2 = np.arange(400, 1150, 10)
    major_ticks_y_2 = np.arange(0, 70000, 5000)
    minor_ticks_y_2 = np.arange(0, 70000, 1000)

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
        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 1100)
        ax.set_ylim(0, 65000)
        ax.legend(loc='upper left', prop={'size': 8})
        ax.set_facecolor('whitesmoke')

    # fig2.suptitle(f' {filename} ', fontsize=20)
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

        ax.grid(which='major', alpha=0.8, lw=.8, ls='--')
        ax.grid(which='minor', alpha=0.6, lw=.6, ls='--')
        ax.set_xlim(400, 900)
        ax.set_facecolor('whitesmoke')

        axs3[0].title.set_text('$15\\degree$ $400\\mu$')
        axs3[1].title.set_text('$15\\degree$ $200\\mu$')

    # fig3.suptitle(f' {filename} ', fontsize=20)
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
    axs4.grid(which='major', alpha=0.8, lw=.8, ls='--')
    axs4.grid(which='minor', alpha=0.6, lw=.6, ls='--')
    axs4.set_xlim(400, 900)
    axs4.set_ylim(min(data.water_indices), max(data.water_indices))
    axs4.set_xlabel('Wavelength [nm]')
    axs4.set_ylabel('Refractive index')
    axs4.set_facecolor('whitesmoke')
    # fig4.suptitle(f' Water indices ', fontsize=20)

    plt.tight_layout()
    plt.margins(0) 

    for i in figs or []:

        plt.close('fig'+i)
    
    plt.show()