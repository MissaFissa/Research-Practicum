import pandas as pd
from pathlib import Path
import numpy as np

cwd = Path.cwd()

class DataGathering:

    def __init__(self):
        
        self.df_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_400 = dict(enumerate(self.df_400))
        self.df_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_200 = dict(enumerate(self.df_200))
        self.t_200 = list(self.info_200.iloc[0])
        self.t_400 = list(self.info_400.iloc[0])
        self.wavelengths = self.df_400[self.dict_400[0]]
        self.wavelengths_400nm = self.df_400[self.dict_400[0]][400:]
        self.dark_200 = []
        self.good_200 = []
        self.dark_400 = []
        self.good_400 = []
        self.n_eff_positive_400_15deg = []
        self.n_eff_negative_400_15deg = []
        self.n_eff_positive_200_15deg = []
        self.n_eff_negative_200_15deg = []
        self.n_eff_positive_400_unscaled_15deg = []
        self.n_eff_negative_400_unscaled_15deg = []
        self.n_eff_positive_200_unscaled_15deg = []
        self.n_eff_negative_200_unscaled_15deg = []
        self.n_eff_positive_400_0deg = []
        self.n_eff_negative_400_0deg = []
        self.n_eff_positive_200_0deg = []
        self.n_eff_negative_200_0deg = []
        self.n_eff_positive_400_unscaled_0deg = []
        self.n_eff_negative_400_unscaled_0deg = []
        self.n_eff_positive_200_unscaled_0deg = []
        self.n_eff_negative_200_unscaled_0deg = []
        self.n_eff_400_15deg_test = []
        self.n_eff_400_0deg_test = []
        self.n_eff_200_15deg_test = []
        self.n_eff_200_0deg_test = []
        self.n_eff_400_unscaled_15deg_test = []
        self.n_eff_400_unscaled_0deg_test = []
        self.n_eff_200_unscaled_15deg_test = []
        self.n_eff_200_unscaled_0deg_test = []
        self.n_eff_test = []
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.t_reference = 6
        self.unscaled_400 = []
        self.unscaled_400_light = []
        self.unscaled_400_dark = []
        self.unscaled_200 = []
        self.unscaled_200_light = []
        self.unscaled_200_dark = []
        self.scaled_400 = []
        self.scaled_400_light = []
        self.scaled_400_dark = []
        self.scaled_200 = []
        self.scaled_200_light = []
        self.scaled_200_dark = []
        self.corrected_400 = []
        self.corrected_200 = []

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

            for j in range(len(self.df_400)):

                corrected_400 = self.df_400[self.good_400[i]][j] - self.df_400[self.dark_400[i]][j]
                corrected_200 = self.df_200[self.good_200[i]][j] - self.df_200[self.dark_200[i]][j]

                corrected_400_temp.append(corrected_400)
                corrected_200_temp.append(corrected_200)

            self.corrected_400.append(corrected_400_temp)
            self.corrected_200.append(corrected_200_temp)

    def scale(self):

        for i in range(1,13):

            self.unscaled_400.append(self.df_400[self.dict_400[i]])
            self.unscaled_200.append(self.df_200[self.dict_200[i]])
                    
            scale_factor_400 = self.t_reference / self.t_400[i-1]
            scale_factor_200 = self.t_reference / self.t_200[i-1]
            
            self.scaled_400.append(scale_factor_400 * self.unscaled_400[i-1])
            self.scaled_200.append(scale_factor_200 * self.unscaled_200[i-1])

            if (i - 1) % 2 == 0:

                self.unscaled_400_light.append(self.unscaled_400[i-1])
                self.unscaled_200_light.append(self.unscaled_200[i-1])

                self.scaled_200_light.append(self.scaled_200[i-1])
                self.scaled_400_light.append(self.scaled_400[i-1])

            else: 

                self.unscaled_400_dark.append(self.unscaled_400[i-1])
                self.unscaled_200_dark.append(self.unscaled_200[i-1])
                
                self.scaled_200_dark.append(self.scaled_200[i-1])
                self.scaled_400_dark.append(self.scaled_400[i-1])

    def effective_index(self):

        b = self.n_air
        c = self.n_water

        for i in range(400,len(self.df_400)):

            a_400_15_deg = ((self.scaled_400_light[0][i] - self.scaled_400_dark[0][i]) / (self.scaled_400_light[5][i] - self.scaled_400_dark[5][i])) ** 0.5
            a_400_0_deg = ((self.scaled_400_light[1][i] - self.scaled_400_dark[1][i]) / (self.scaled_400_light[4][i] - self.scaled_400_dark[4][i])) ** 0.5

            n_eff_400_15deg = ((-1 * (c - b + a_400_15_deg * (c - b)) - ((c - b + a_400_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg)))
            n_eff_400_0deg = ((-1 * (c - b + a_400_0_deg * (c - b)) - ((c - b + a_400_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_0_deg)))

            self.n_eff_400_15deg_test.append(n_eff_400_15deg)
            self.n_eff_400_0deg_test.append(n_eff_400_0deg)

            a_200_15_deg = ((self.scaled_200_light[0][i] - self.scaled_200_dark[0][i]) / (self.scaled_200_light[5][i] - self.scaled_200_dark[5][i])) ** 0.5
            a_200_0_deg = ((self.scaled_200_light[1][i] - self.scaled_200_dark[1][i]) / (self.scaled_200_light[4][i] - self.scaled_200_dark[4][i])) ** 0.5

            n_eff_200_15deg = ((-1 * (c - b + a_200_15_deg * (c - b)) - ((c - b + a_200_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg)))
            n_eff_200_0deg = ((-1 * (c - b + a_200_0_deg * (c - b)) - ((c - b + a_200_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_0_deg)))

            self.n_eff_200_15deg_test.append(n_eff_200_15deg)
            self.n_eff_200_0deg_test.append(n_eff_200_0deg)
            
            a_400_15_deg_unscaled = ((self.unscaled_400_light[0][i] - self.unscaled_400_dark[0][i]) / (self.unscaled_400_light[5][i] - self.unscaled_400_dark[5][i])) ** 0.5
            a_400_0_deg_unscaled = ((self.unscaled_400_light[1][i] - self.unscaled_400_dark[1][i]) / (self.unscaled_400_light[4][i] - self.unscaled_400_dark[4][i])) ** 0.5

            n_eff_400_15deg_unscaled = ((-1 * (c - b + a_400_15_deg_unscaled * (c - b)) - ((c - b + a_400_15_deg_unscaled * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg_unscaled) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg_unscaled)))
            n_eff_400_0deg_unscaled = ((-1 * (c - b + a_400_0_deg_unscaled * (c - b)) - ((c - b + a_400_0_deg_unscaled * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_0_deg_unscaled) ** 2))) ** 0.5) / (2 * (1 - a_400_0_deg_unscaled)))

            self.n_eff_400_unscaled_15deg_test.append(n_eff_400_15deg_unscaled)
            self.n_eff_400_unscaled_0deg_test.append(n_eff_400_0deg_unscaled)

            a_200_15_deg_unscaled = ((self.unscaled_200_light[0][i] - self.unscaled_200_dark[0][i]) / (self.unscaled_200_light[5][i] - self.unscaled_200_dark[5][i])) ** 0.5
            a_200_0_deg_unscaled = ((self.unscaled_200_light[1][i] - self.unscaled_200_dark[1][i]) / (self.unscaled_200_light[4][i] - self.unscaled_200_dark[4][i])) ** 0.5

            n_eff_200_15deg_unscaled = ((-1 * (c - b + a_200_15_deg_unscaled * (c - b)) - ((c - b + a_200_15_deg_unscaled * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg_unscaled) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg_unscaled)))
            n_eff_200_0deg_unscaled = ((-1 * (c - b + a_200_0_deg_unscaled * (c - b)) - ((c - b + a_200_0_deg_unscaled * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_0_deg_unscaled) ** 2))) ** 0.5) / (2 * (1 - a_200_0_deg_unscaled)))

            self.n_eff_200_unscaled_15deg_test.append(n_eff_200_15deg_unscaled)
            self.n_eff_200_unscaled_0deg_test.append(n_eff_200_0deg_unscaled)
            
data = DataGathering()
data.background_correction()
data.scale()
data.effective_index_15deg()
data.effective_index_0deg()
data.test_effective_index_15deg()