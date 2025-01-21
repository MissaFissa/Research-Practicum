from research_practicum.data_gathering import DataGathering

class Analysis:

    def __init__(self):
        
        filename_400 = 'data_400mu_csv/12_measurements_400mu'
        filename_200 = 'data_200mu_csv/12_measurements_200mu'
        filename_test = (f'{filename_400},{filename_200}')        
        test = DataGathering(filename_test) 
        self.n_air = test.n_air
        self.scaled_400_test = test.scaled_400
        self.scaled_200_test = test.scaled_200
        self.good_400 = test.good_400
        self.good_200 = test.good_200
        self.n_eff_400_0deg_test = test.n_eff_400_0deg
        self.n_eff_200_0deg_test = test.n_eff_200_0deg
        self.R_IL_400 = []
        self.R_IL_200 = []

    def fresnel_reflection(self, n_eff, n_sample):
        
        return ((n_eff - n_sample) ** 2) / ((n_eff + n_sample) ** 2)

    def ref_abs(self, R_ref, I_sample, I_ref):

        return R_ref * (I_sample / I_ref)
    
    def ref_calibration(self):

        for i in range(len(self.n_eff_400_0deg_test)):

            R_air_400 = self.fresnel_reflection(self.n_eff_400_0deg_test[i], self.n_air)
            R_air_200 = self.fresnel_reflection(self.n_eff_200_0deg_test[i], self.n_air)

            I_sample_400 = self.scaled_400_test[self.good_400.index('400 mu 6 ms 0 deg IL')][i]
            I_sample_200 = self.scaled_200_test[self.good_200.index('200 mu 5.1 ms 0 deg IL')][i]

            I_air_400 = self.scaled_400_test[self.good_400.index('400 mu 6 ms 0 deg fresnel')][i]
            I_air_200 = self.scaled_200_test[self.good_200.index('fresnel 200 mu 5 ms 0 deg ')][i]

            self.R_IL_400.append(self.ref_abs(R_air_400, I_sample_400, I_air_400))
            self.R_IL_200.append(self.ref_abs(R_air_200, I_sample_200, I_air_200))

    def ref_experiment(self):
        
        for i in range(len(self.scaled_400_test)):

            I_IL_15_400 = self.scaled_400_test[3][i] - self.scaled_400_test[4][i]
            I_IL_15_200 = self.scaled_200_test[3][i] - self.scaled_200_test[4][i]

analysis = Analysis()
