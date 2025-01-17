import pandas as pd
from pathlib import Path
import numpy as np

cwd = Path.cwd()

class DataTests:

    def __init__(self):
        
        self.df_water = pd.read_csv(f'{cwd}/literature_data/Hale.csv', sep=',')
        self.dict_water = dict(enumerate(self.df_water))
        self.wavelengths_water = self.df_water[self.dict_water[0]].astype(float)
        self.indices_water = self.df_water[self.dict_water[1]].astype(float)

        self.df_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_400 = dict(enumerate(self.df_400))

        self.df_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_200 = dict(enumerate(self.df_200))

        self.t_400 = list(dict.fromkeys(self.info_400.iloc[0]))
        self.t_200 = list(dict.fromkeys(self.info_200.iloc[0]))
   
        self.n_eff_400_15deg = []
        self.n_eff_400_0deg = []
        self.n_eff_200_15deg = []
        self.n_eff_200_0deg = []
        self.scaled_400 = []
        self.scaled_200 = []
        self.dark_400 = []
        self.dark_200 = []
        self.good_400 = []
        self.good_200 = []
        self.corrected_400 = []
        self.corrected_200 = []
        self.water_indices = []

        self.index_wl400nm = 451
        self.wavelengths = self.df_400[self.dict_400[0]]
        self.wavelengths_400nm = self.df_400[self.dict_400[0]][self.index_wl400nm:]
        self.t_reference = 6
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.B1 = 0.75831
        self.C1 = 0.01007
        self.B2 = 0.08495
        self.C2 = 8.91377

    def background_correction(self):

        for i in range(1,len(self.dict_400)):

            if 'dark' in self.dict_200[i]:

                self.dark_200.append(self.dict_200[i])

            if 'dark' in self.dict_400[i]:

                self.dark_400.append(self.dict_400[i])

            else:

                self.good_200.append(self.dict_200[i])
                self.good_400.append(self.dict_400[i])

        for i in range(len(self.good_400)):

            corrected_400_temp = []
            corrected_200_temp = []

            for j in range(self.index_wl400nm, len(self.df_400)):

                corrected_400 = self.df_400[self.good_400[i]][j] - self.df_400[self.dark_400[i]][j]
                corrected_200 = self.df_200[self.good_200[i]][j] - self.df_200[self.dark_200[i]][j]

                corrected_400_temp.append(corrected_400)
                corrected_200_temp.append(corrected_200)

            self.corrected_400.append(corrected_400_temp)
            self.corrected_200.append(corrected_200_temp)

        self.corrected_400_array = np.array(self.corrected_400)
        self.corrected_200_array = np.array(self.corrected_200)

    def scale(self):

        for i in range(len(self.corrected_400)):

            scale_factor_400 = self.t_reference / self.t_400[i]
            scale_factor_200 = self.t_reference / self.t_200[i]
            
            self.scaled_400.append(scale_factor_400 * self.corrected_400_array[i])
            self.scaled_200.append(scale_factor_200 * self.corrected_200_array[i])

    def sellmeier(self):
        
        for wl in self.wavelengths_400nm / 1000:
            
            n = (1 + ((self.B1 * wl ** 2) / (wl ** 2 - self.C1)) + ((self.B2 * wl ** 2) / (wl ** 2 - self.C2))) ** 0.5
            
            self.water_indices.append(n)

    def effective_index(self):

        b = self.n_air

        for i in range(len(self.scaled_400[0])):
            
            c = self.water_indices[i]

            a_400_15_deg = (self.scaled_400[0][i] / self.scaled_400[5][i]) ** 0.5
            a_400_0_deg = (self.scaled_400[1][i] / self.scaled_400[4][i]) ** 0.5
            n_eff_400_15deg = ((-1 * (c - b + a_400_15_deg * (c - b)) - ((c - b + a_400_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg)))
            n_eff_400_0deg = ((-1 * (c - b + a_400_0_deg * (c - b)) - ((c - b + a_400_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_0_deg)))

            self.n_eff_400_15deg.append(n_eff_400_15deg)
            self.n_eff_400_0deg.append(n_eff_400_0deg)

            a_200_15_deg = (self.scaled_200[0][i] / self.scaled_200[5][i]) ** 0.5
            a_200_0_deg = (self.scaled_200[1][i] / self.scaled_200[4][i]) ** 0.5

            n_eff_200_15deg = ((-1 * (c - b + a_200_15_deg * (c - b)) - ((c - b + a_200_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg)))
            n_eff_200_0deg = ((-1 * (c - b + a_200_0_deg * (c - b)) - ((c - b + a_200_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_0_deg)))

            self.n_eff_200_15deg.append(n_eff_200_15deg)
            self.n_eff_200_0deg.append(n_eff_200_0deg)

class DataExperiment:

    def __init__(self):
        
        self.df_water = pd.read_csv(f'{cwd}/literature_data/Hale.csv', sep=',')
        self.dict_water = dict(enumerate(self.df_water))
        self.wavelengths_water = self.df_water[self.dict_water[0]].astype(float)
        self.indices_water = self.df_water[self.dict_water[1]].astype(float)

        self.df_experiment = pd.read_csv(f'{cwd}/data/data_experiment/experiment.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_experiment = pd.read_csv(f'{cwd}/data/data_experiment/experiment.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_experiment = dict(enumerate(self.df_experiment))
        self.df_200_experiment = self.df_experiment.iloc[:, [ i for i in range(1, (len(self.dict_experiment) // 2) + 1)]]
        self.df_400_experiment = self.df_experiment.iloc[:, (len(self.dict_experiment) // 2) + 1:]
        self.dict_400_experiment = dict(enumerate(self.df_400_experiment))
        self.dict_200_experiment = dict(enumerate(self.df_200_experiment))

        self.t_experiment = list(dict.fromkeys(self.info_experiment.iloc[0]))

        self.n_eff_400_15deg_experiment = []
        self.n_eff_200_15deg_experiment = []

        self.scaled_400_experiment = []
        self.scaled_200_experiment = []
        self.dark_400_experiment = []
        self.dark_200_experiment = []
        self.good_400_experiment = []
        self.good_200_experiment = []
        self.corrected_400_experiment = []
        self.corrected_200_experiment = []
        self.water_indices = []

        self.index_wl400nm = 451
        self.wavelengths = self.df_experiment[self.dict_experiment[0]]
        self.wavelengths_400nm = self.df_experiment[self.dict_experiment[0]][self.index_wl400nm:]
        self.t_reference = 6
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.B1 = 0.75831
        self.C1 = 0.01007
        self.B2 = 0.08495
        self.C2 = 8.91377

    def background_correction(self):

        for i in range(len(self.dict_400_experiment)):

            if 'dark' in self.dict_400_experiment[i]:

                self.dark_400_experiment.append(self.dict_400_experiment[i])

            if 'dark' in self.dict_200_experiment[i]:

                self.dark_200_experiment.append(self.dict_200_experiment[i])

            else:

                self.good_400_experiment.append(self.dict_400_experiment[i])
                self.good_200_experiment.append(self.dict_200_experiment[i])
                
        for i in range(len(self.good_400_experiment)):

            corrected_400_experiment_temp = []
            corrected_200_experiment_temp = []

            # for j in range(self.index_wl400nm, len(self.df_experiment)):

            #     corrected_400_experiment = self.df_experiment[self.good_400_experiment[i]][j] - self.df_experiment[self.dark_400_experiment[i]][j]
            #     corrected_200_experiment = self.df_experiment[self.good_200_experiment[i]][j] - self.df_experiment[self.dark_200_experiment[i]][j]

            #     corrected_400_experiment_temp.append(corrected_400_experiment)
            #     corrected_200_experiment_temp.append(corrected_200_experiment)

            for j in range(self.index_wl400nm, len(self.df_400_experiment)):

                corrected_400_experiment = self.df_400_experiment[self.good_400_experiment[i]][j] - self.df_400_experiment[self.dark_400_experiment[i]][j]
                corrected_200_experiment = self.df_200_experiment[self.good_200_experiment[i]][j] - self.df_200_experiment[self.dark_200_experiment[i]][j]

                corrected_400_experiment_temp.append(corrected_400_experiment)
                corrected_200_experiment_temp.append(corrected_200_experiment)

            self.corrected_400_experiment.append(corrected_400_experiment_temp)
            self.corrected_200_experiment.append(corrected_200_experiment_temp)

        self.corrected_400_experiment_array = np.array(self.corrected_400_experiment)
        self.corrected_200_experiment_array = np.array(self.corrected_200_experiment)

    def scale(self):

        for i in range(len(self.corrected_400_experiment)):

            # scale_factor_400_experiment = self.t_reference / self.t_experiment[:len(self.t_experiment) // 2][i]
            # scale_factor_200_experiment = self.t_reference / self.t_experiment[len(self.t_experiment) // 2:][i]
            scale_factor_400_experiment = self.t_reference / self.t_experiment[:len(self.t_experiment) // 2][i]
            scale_factor_200_experiment = self.t_reference / self.t_experiment[len(self.t_experiment) // 2:][i]
            
            self.scaled_400_experiment.append(scale_factor_400_experiment * self.corrected_400_experiment_array[i])
            self.scaled_200_experiment.append(scale_factor_200_experiment * self.corrected_200_experiment_array[i])

    def sellmeier(self):
        
        for wl in self.wavelengths_400nm / 1000:
            
            n = (1 + ((self.B1 * wl ** 2) / (wl ** 2 - self.C1)) + ((self.B2 * wl ** 2) / (wl ** 2 - self.C2))) ** 0.5
            
            self.water_indices.append(n)

    # def effective_index(self):

    #     b = self.n_air

    #     for i in range(len(self.scaled_400_experiment[0])):
            
    #         c = self.water_indices[i]

    #         a_400_15_deg = (self.scaled_400_experiment[0][i] / self.scaled_400_experiment[5][i]) ** 0.5
    #         n_eff_400_15deg = ((-1 * (c - b + a_400_15_deg * (c - b)) - ((c - b + a_400_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg)))

    #         self.n_eff_400_15deg_experiment.append(n_eff_400_15deg)

    #         a_200_15_deg = (self.scaled_200_experiment[0][i] / self.scaled_200_experiment[5][i]) ** 0.5

    #         n_eff_200_15deg = ((-1 * (c - b + a_200_15_deg * (c - b)) - ((c - b + a_200_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg)))

    #         self.n_eff_200_15deg_experiment.append(n_eff_200_15deg)

test = DataTests()
test.background_correction()
test.scale()
test.sellmeier()
test.effective_index()

data = DataExperiment()
data.background_correction()
data.scale()
data.sellmeier()
# data.effective_index()

# print(test.scaled_400)
print(len(data.scaled_400_experiment))
print(data.dict_400_experiment)
# print(data.scaled_200_experiment)