import pandas as pd
from pathlib import Path

cwd = Path.cwd()

class DataGathering:

    def __init__(self):
        
        self.df_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_400 = pd.read_csv(f'{cwd}/data/data_400mu_csv/12_measurements_400mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_400 = dict(enumerate(self.df_400))
        self.df_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', skiprows=[0,1,2,3,4], header=[0], decimal=',')
        self.info_200 = pd.read_csv(f'{cwd}/data/data_200mu_csv/12_measurements_200mu.csv', sep=';', index_col=0, nrows=2, skiprows=[1,4], decimal=',')
        self.dict_200 = dict(enumerate(self.df_200))
        self.t200 = list(self.info_200.iloc[0])
        self.t400 = list(self.info_400.iloc[0])
        self.wavelengths = self.df_400[self.dict_400[0]]

        self.fresnel_200_5ms_0deg = self.df_200[self.dict_200[3]]
        self.fresnel_200_5ms_0deg_dark = self.df_200[self.dict_200[4]]
        self.fresnel_200_1400ms_15deg = self.df_200[self.dict_200[1]]
        self.fresnel_200_1400ms_15deg_dark = self.df_200[self.dict_200[2]]

        self.fresnel_400_6ms_0deg = self.df_400[self.dict_400[3]]
        self.fresnel_400_6ms_0deg_dark = self.df_400[self.dict_400[4]]
        self.fresnel_400_280ms_15deg = self.df_400[self.dict_400[1]]
        self.fresnel_400_280ms_15deg_dark = self.df_400[self.dict_400[2]]

        self.water_200_73ms_0deg = self.df_200[v[11]]
        self.water_200_73ms_0deg_dark = self.df_200[self.dict_200[12]]
        self.water_200_1600ms_15deg = self.df_200[self.dict_200[9]]
        self.water_200_1600ms_15deg_dark = self.df_200[self.dict_200[10]]

        self.water_400_107ms_0deg = self.df_400[self.dict_400[9]]
        self.water_400_107ms_0deg_dark = self.df_400[self.dict_400[10]]
        self.water_400_2000ms_15deg = self.df_400[self.dict_400[11]]
        self.water_400_2000ms_15deg_dark = self.df_400[self.dict_400[12]]

        self.IL_200_5ms_0deg = self.df_200[self.dict_200[7]]
        self.IL_200_5ms_0deg_dark = self.df_200[self.dict_200[8]]
        self.IL_200_5ms_15deg = self.df_200[self.dict_200[5]]
        self.IL_200_5ms_15deg_dark = self.df_200[self.dict_200[6]]

        self.IL_400_6ms_0deg = self.df_400[self.dict_400[7]]
        self.IL_400_6ms_0deg_dark = self.df_400[self.dict_400[8]]
        self.IL_400_6ms_15deg = self.df_400[self.dict_400[5]]
        self.IL_400_6ms_15deg_dark = self.df_400[self.dict_400[6]]

        self.corrected_fresnel_400_6ms_0deg = self.fresnel_400_6ms_0deg - self.fresnel_400_6ms_0deg_dark
        self.corrected_fresnel_400_280ms_15deg = self.fresnel_400_280ms_15deg - self.fresnel_400_280ms_15deg_dark
        self.corrected_fresnel_200_280ms_0deg = self.fresnel_200_5ms_0deg - self.fresnel_200_5ms_0deg_dark
        self.corrected_fresnel_200_1400ms_15deg = self.fresnel_200_1400ms_15deg - self.fresnel_200_1400ms_15deg_dark
        self.corrected_water_400_107ms_0deg = self.water_400_107ms_0deg - self.water_400_107ms_0deg_dark
        self.corrected_water_400_2000ms_15deg = self.water_400_2000ms_15deg - self.water_400_2000ms_15deg_dark
        self.corrected_water_200_73ms_0deg = self.water_200_73ms_0deg - self.water_200_73ms_0deg_dark
        self.corrected_water_200_1600ms_15deg = self.water_200_1600ms_15deg - self.water_200_1600ms_15deg_dark
        self.corrected_IL_400_6ms_0deg = self.IL_400_6ms_0deg - self.IL_400_6ms_0deg_dark
        self.corrected_IL_400_6ms_15deg = self.IL_400_6ms_15deg - self.IL_400_6ms_15deg_dark
        self.corrected_IL_200_5ms_0deg = self.IL_200_5ms_0deg - self.IL_200_5ms_15deg_dark
        self.corrected_IL_200_5ms_15deg = self.IL_200_5ms_15deg - self.IL_200_5ms_15deg_dark

