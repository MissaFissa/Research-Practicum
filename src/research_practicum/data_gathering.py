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
        self.t_200 = None
        self.t_400 = None
        self.dict_200 = None
        self.dict_400 = None
        self.df_200 = None
        self.df_400 = None
        self.n_eff_400_15deg = []
        self.n_eff_200_15deg = []
        self.n_eff_400_0deg = []
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
        self.t_reference = 5
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.B1 = 0.75831
        self.C1 = 0.01007
        self.B2 = 0.08495
        self.C2 = 8.91377
        self.gather_data()

    def gather_data(self):

        if ',' in self.filename:

            filenames = self.filename.split(',')
            filename_400 = filenames[0]
            filename_200 = filenames[1]

            df_400 = pd.read_csv(f'{Path.cwd()}/data/{filename_400}.csv', sep=';',decimal=',', header=[5])
            df_200 = pd.read_csv(f'{Path.cwd()}/data/{filename_200}.csv', sep=';', decimal=',', header=[5])

            df_400_info = pd.read_csv(f'{Path.cwd()}/data/{filename_400}.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
            df_200_info = pd.read_csv(f'{Path.cwd()}/data/{filename_200}.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
            
            df_joined = pd.merge(df_400, df_200, on='Wavelength [nm]')
            df_joined.to_csv(f'{Path.cwd()}/data/test_measurements.csv', index=False)
            df_joined_info = pd.concat([df_400_info, df_200_info], axis=1)
            df_joined_info.to_csv(f'{Path.cwd()}/data/info_test_measurements.csv')
            self.filename = 'test_measurements'
            
        else:

            pass
        
        self.csv_file()

    def csv_file(self):

        if 'test' in self.filename:

            self.df = pd.read_csv(f'{cwd}/data/{self.filename}.csv', sep=',', header=[0])
            self.info = pd.read_csv(f'{cwd}/data/info_{self.filename}.csv', sep=',', index_col=0, nrows=2, skiprows=[2])
            self.dict = dict(enumerate(self.df))
            self.t = self.info.iloc[0].to_list()
            self.wavelengths = self.df[self.dict[0]]
            self.wavelengths_400nm = self.df[self.dict[0]][self.index_wl400nm:]
            self.wavelength_635nm_index = self.wavelengths_400nm[self.wavelengths_400nm == 635.098].index[0] - self.index_wl400nm

        else:

            self.df = pd.read_csv(f'{cwd}/data/{self.filename}.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
            self.info = pd.read_csv(f'{cwd}/data/{self.filename}.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
            self.dict = dict(enumerate(self.df))
            self.t = self.info.iloc[0].to_list()
            self.wavelengths = self.df[self.dict[0]]
            self.wavelengths_400nm = self.df[self.dict[0]][self.index_wl400nm:]
            self.wavelength_635nm_index = self.wavelengths_400nm[self.wavelengths_400nm == 635.098].index[0] - self.index_wl400nm

        self.split_dataframe()

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

        self.background_correction()

    def background_correction(self):
        
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

        self.scale()

    def scale(self):
     
        for i in range(len(self.corrected_400)):

            scale_factor_400 = self.t_reference / self.t_400[i]
            scale_factor_200 = self.t_reference / self.t_200[i]
            self.scaled_400.append(scale_factor_400 * self.corrected_400[i])
            self.scaled_200.append(scale_factor_200 * self.corrected_200[i])

        self.effective_index()

    def sellmeier(self):

        for wl in self.wavelengths_400nm / 1000:
            
            n = (1 + ((self.B1 * wl ** 2) / (wl ** 2 - self.C1)) + ((self.B2 * wl ** 2) / (wl ** 2 - self.C2))) ** 0.5
            
            self.water_indices.append(n)

    def effective_index(self):
        
        if 'bellyfat' not in self.filename:
            
            self.sellmeier()

            b = self.n_air
         
            if 'test' in self.filename:
                
                for i in range(len(self.scaled_400[0])):
                    
                    c = self.water_indices[i]
            
                    a_400_15_deg = (self.scaled_400[self.good_400.index('400 mu 280 ms 15 deg fresnel')][i] / self.scaled_400[self.good_400.index('400 mu 2 s 15 deg water')][i]) ** 0.5
                    a_400_0_deg = (self.scaled_400[self.good_400.index('400 mu 6 ms 0 deg fresnel')][i] / self.scaled_400[self.good_400.index('400 mu 107 ms 0 deg water')][i]) ** 0.5

                    n_eff_400_15deg = ((-1 * (c - b + a_400_15_deg * (c - b)) - ((c - b + a_400_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_15_deg)))
                    n_eff_400_0deg = ((-1 * (c - b + a_400_0_deg * (c - b)) - ((c - b + a_400_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_400_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_400_0_deg)))

                    self.n_eff_400_15deg.append(n_eff_400_15deg)
                    self.n_eff_400_0deg.append(n_eff_400_0deg)

                    a_200_15_deg = (self.scaled_200[self.good_200.index('fresnel 200 mu 1.4 s 15 deg')][i] / self.scaled_200[self.good_200.index('200 mu 1.6 s 15 deg water ')][i]) ** 0.5
                    a_200_0_deg = (self.scaled_200[self.good_200.index('fresnel 200 mu 5 ms 0 deg ')][i] / self.scaled_200[self.good_200.index('200 mu 73 ms 0 deg water ')][i]) ** 0.5

                    n_eff_200_15deg = ((-1 * (c - b + a_200_15_deg * (c - b)) - ((c - b + a_200_15_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_15_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_15_deg)))
                    n_eff_200_0deg = ((-1 * (c - b + a_200_0_deg * (c - b)) - ((c - b + a_200_0_deg * (c - b)) ** 2 + (4 * b * c * ((1 - a_200_0_deg) ** 2))) ** 0.5) / (2 * (1 - a_200_0_deg)))

                    self.n_eff_200_15deg.append(n_eff_200_15deg)
                    self.n_eff_200_0deg.append(n_eff_200_0deg)

            else:
               
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