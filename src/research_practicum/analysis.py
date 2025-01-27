from research_practicum.data_gathering import DataGathering

class Analysis:

    def __init__(self):
        
        filename_400 = 'data_400mu_csv/12_measurements_400mu'
        filename_200 = 'data_200mu_csv/12_measurements_200mu'
        filename_experiment = 'data_experiment/bellyfat'
        filename_test = (f'{filename_400},{filename_200}') 
        test = DataGathering(filename_test) 
        exp = DataGathering(filename_experiment)
        self.n_air = test.n_air
        self.wavelengths_400nm = test.wavelengths_400nm
        self.wavelength_635nm_index = test.wavelength_635nm_index
        self.scaled_400_test = test.scaled_400
        self.scaled_200_test = test.scaled_200
        self.scaled_400_exp = exp.scaled_400
        self.scaled_200_exp = exp.scaled_200
        self.good_400_test = test.good_400
        self.good_200_test = test.good_200
        self.good_400_exp = exp.good_400
        self.good_200_exp = exp.good_200
        self.n_eff_400_0deg_test = test.n_eff_400_0deg
        self.n_eff_200_0deg_test = test.n_eff_200_0deg
        self.R_IL_400 = []
        self.R_IL_200 = []
        self.R_fat_400 = []
        self.R_fat_200 = []
        self.R_muscle_400 = []
        self.R_muscle_200 = []
        self.R_redmuscle_400 = []
        self.R_redmuscle_200 = []
        self.R_skin_400 = []
        self.R_skin_200 = []
        self.ref_calibration()

    def fresnel_reflection(self, n_eff, n_sample):
        
        return ((n_eff - n_sample) ** 2) / ((n_eff + n_sample) ** 2)

    def ref_abs(self, R_ref, I_sample, I_ref):

        return R_ref * (I_sample / I_ref)
    
    def ref_calibration(self):

        for i in range(len(self.n_eff_400_0deg_test)):

            R_air_400 = self.fresnel_reflection(self.n_eff_400_0deg_test[i], self.n_air)
            R_air_200 = self.fresnel_reflection(self.n_eff_200_0deg_test[i], self.n_air)

            I_sample_400 = self.scaled_400_test[self.good_400_test.index('400 mu 6 ms 0 deg IL')][i]
            I_sample_200 = self.scaled_200_test[self.good_200_test.index('200 mu 5.1 ms 0 deg IL')][i]

            I_air_400 = self.scaled_400_test[self.good_400_test.index('400 mu 6 ms 0 deg fresnel')][i]
            I_air_200 = self.scaled_200_test[self.good_200_test.index('fresnel 200 mu 5 ms 0 deg ')][i]

            self.R_IL_400.append(self.ref_abs(R_air_400, I_sample_400, I_air_400))
            self.R_IL_200.append(self.ref_abs(R_air_200, I_sample_200, I_air_200))

        self.ref_experiment()

    def ref_experiment(self):
        
        for i in range(len(self.n_eff_400_0deg_test)):

            I_IL_15_400 = self.scaled_400_test[self.good_400_test.index('400 mu 6 ms 0 deg IL')][i] - self.scaled_400_test[self.good_400_test.index('400 mu 107 ms 0 deg water')][i]
            I_IL_15_200 = self.scaled_200_test[self.good_200_test.index('200 mu 5.1 ms 0 deg IL')][i] - self.scaled_200_test[self.good_200_test.index('200 mu 73 ms 0 deg water ')][i]

            # I_IL_15_400 = self.scaled_400_test[self.good_400_test.index('400 mu 5.5 ms 15 deg IL')][i]
            # I_IL_15_200 = self.scaled_200_test[self.good_200_test.index('200 mu 4.5 ms 15 deg IL')][i]

            I_sample_400_fat = self.scaled_400_exp[self.good_400_exp.index('400 mu 36 ms 15 deg fat')][i]
            I_sample_400_muscle = self.scaled_400_exp[self.good_400_exp.index('400 mu 59 ms 15 deg muscle')][i]
            I_sample_400_redmuscle = self.scaled_400_exp[self.good_400_exp.index('400 mu 80 ms 15 deg red muscle')][i]
            I_sample_400_skin = self.scaled_400_exp[self.good_400_exp.index('400 mu 25 ms 15 deg skin')][i]

            I_sample_200_fat = self.scaled_200_exp[self.good_200_exp.index('200 mu 26 ms 15 deg fat')][i]
            I_sample_200_muscle = self.scaled_200_exp[self.good_200_exp.index('200 mu 42 ms 15 deg muscle')][i]
            I_sample_200_redmuscle = self.scaled_200_exp[self.good_200_exp.index('200 mu 53 ms 15 deg red muscle')][i]
            I_sample_200_skin = self.scaled_200_exp[self.good_200_exp.index('200 mu 11 ms 15 deg skin')][i]

            self.R_fat_400.append(self.ref_abs(self.R_IL_400[i], I_sample_400_fat, I_IL_15_400))
            self.R_muscle_400.append(self.ref_abs(self.R_IL_400[i], I_sample_400_muscle, I_IL_15_400))
            self.R_redmuscle_400.append(self.ref_abs(self.R_IL_400[i], I_sample_400_redmuscle, I_IL_15_400))
            self.R_skin_400.append(self.ref_abs(self.R_IL_400[i], I_sample_400_skin, I_IL_15_400))

            self.R_fat_200.append(self.ref_abs(self.R_IL_200[i], I_sample_200_fat, I_IL_15_200))
            self.R_muscle_200.append(self.ref_abs(self.R_IL_200[i], I_sample_200_muscle, I_IL_15_200))
            self.R_redmuscle_200.append(self.ref_abs(self.R_IL_200[i], I_sample_200_redmuscle, I_IL_15_200))
            self.R_skin_200.append(self.ref_abs(self.R_IL_200[i], I_sample_200_skin, I_IL_15_200))