import pandas as pd
import numpy as np
from pathlib import Path

cwd = Path.cwd()

class DataGathering():

    def __init__(self, filename):

        self.filename = filename
        self.df_water = pd.read_csv(f'{cwd}/literature_data/Hale.csv', sep=',')
        self.dict_water = dict(enumerate(self.df_water))
        self.wavelengths_water = self.df_water[self.dict_water[0]].astype(float)
        self.indices_water = self.df_water[self.dict_water[1]].astype(float)
        
        self.df = pd.read_csv(f'{cwd}/data/data_experiment/{filename}.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info = pd.read_csv(f'{cwd}/data/data_experiment/{filename}.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict = dict(enumerate(self.df))
        self.t = self.info.iloc[0].to_list()
        self.t_200 = None
        self.t_400 = None
        self.dict_200 = None
        self.dict_400 = None
        self.df_200 = None
        self.df_400 = None
        self.n_eff_400_15deg = []
        self.n_eff_200_15deg = []
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
        self.wavelengths = self.df[self.dict[0]]
        self.wavelengths_400nm = self.df[self.dict[0]][self.index_wl400nm:]
        self.t_reference = 5
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.B1 = 0.75831
        self.C1 = 0.01007
        self.B2 = 0.08495
        self.C2 = 8.91377

    def split_dataframe(self):
        
        dict_200_temp = {}
        dict_400_temp = {}
        t_200_temp = []
        t_400_temp = []

        for k, v in self.dict.items():

            if '200' in v:

                dict_200_temp.update({v:self.df[v]})
                t_200_temp.append(self.t[k-1])

            if '400' in v:

                dict_400_temp.update({v:self.df[v]})
                t_400_temp.append(self.t[k-1])

        self.df_200 = pd.DataFrame.from_dict(dict_200_temp)
        self.df_400 = pd.DataFrame.from_dict(dict_400_temp)
        self.dict_200 = dict(enumerate(self.df_200))
        self.dict_400 = dict(enumerate(self.df_400))
        self.t_200 = list(dict.fromkeys(t_200_temp))
        self.t_400 = list(dict.fromkeys(t_400_temp))

    def background_correction(self):
        
        self.split_dataframe()

        for i in range(len(self.dict_400)):

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

        self.corrected_400 = np.array(self.corrected_400)
        self.corrected_200 = np.array(self.corrected_200)

    def scale(self):

        self.background_correction()

        for i in range(len(self.corrected_400)):

            scale_factor_400 = self.t_reference / self.t_400[i]
            scale_factor_200 = self.t_reference / self.t_200[i]
            self.scaled_400.append(scale_factor_400 * self.corrected_400[i])
            self.scaled_200.append(scale_factor_200 * self.corrected_200[i])

    def sellmeier(self):
        
        for wl in self.wavelengths_400nm / 1000:
            
            n = (1 + ((self.B1 * wl ** 2) / (wl ** 2 - self.C1)) + ((self.B2 * wl ** 2) / (wl ** 2 - self.C2))) ** 0.5
            
            self.water_indices.append(n)

    def effective_index(self):
        
        self.scale()

        if 'bellyfat' not in self.filename:
            
            self.sellmeier()

            b = self.n_air

            for i in range(len(self.scaled_400[0])):
                
                c = self.water_indices[i]

                a_400_15_deg = (self.scaled_400[0][i] / self.scaled_400[2][i]) ** 0.5
                n_eff_400_15deg = ((-1 * (c - b + a_400_15_deg * (c - b)) - ((c - b + a_400_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg)))

                self.n_eff_400_15deg.append(n_eff_400_15deg)

                a_200_15_deg = (self.scaled_200[0][i] / self.scaled_200[2][i]) ** 0.5

                n_eff_200_15deg = ((-1 * (c - b + a_200_15_deg * (c - b)) - ((c - b + a_200_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg)))

                self.n_eff_200_15deg.append(n_eff_200_15deg)

        else:

            return            