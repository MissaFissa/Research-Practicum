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
        self.t_200 = list(self.info_200.iloc[0])
        self.t_400 = list(self.info_400.iloc[0])
        self.wavelengths = self.df_400[self.dict_400[0]]
        self.dark_200 = []
        self.good_200 = []
        self.dark_400 = []
        self.good_400 = []
        self.NA = 0.39
        self.n_water = 1.33
        self.n_air = 1.0
        self.t_reference = 5
        self.unscaled_400 = []
        self.unscaled_200 = []
        self.scaled_400 = []
        self.scaled_200 = []

    def background(self):

        for i in range(1,len(self.dict_400)):
            
            if 'dark' in self.dict_200[i]:

                self.dark_200.append(self.dict_200[i])

            if 'dark' in self.dict_400[i]:

                self.dark_400.append(self.dict_400[i])

            else:

                self.good_200.append(self.dict_200[i])
                self.good_400.append(self.dict_400[i])

    def scale(self):

        for i in range(1,13):

            self.unscaled_400.append(self.df_400[self.dict_400[i]])
            self.unscaled_200.append(self.df_200[self.dict_200[i]])
        
        for i in range(1,13):
            
            scale_factor_400 = self.t_reference / self.t_400[i - 1]
            scale_factor_200 = self.t_reference / self.t_200[i - 1]
            
            self.scaled_400.append(scale_factor_400 * self.unscaled_400[i-1])

data = DataGathering()
data.scale()
print(data.scaled_400[0][0:10])
print(data.unscaled_400[0][0:10])
