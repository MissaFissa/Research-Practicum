from research_practicum.data_gathering import DataGathering, cwd

class Analysis:

    def __init__(self):
        
        filename_400 = 'data_400mu_csv/12_measurements_400mu'
        filename_200 = 'data_200mu_csv/12_measurements_200mu'
        filename_test = (f'{filename_400},{filename_200}')        
        test = DataGathering(filename_test) 
        self.scaled_400_test = test.scaled_400
        self.scaled_200_test = test.scaled_200
        self.n_eff_400_0deg_test = test.n_eff_400_0deg
        self.n_eff_200_0deg_test = test.n_eff_200_0deg

        self.ref_fres_400 = []
        self.ref_fres_200 = []
        self.abs_ref_400 = []
        self.abs_ref_200 = []


    def fresnel_reflection(self):
        
        for i in range(len(self.n_eff_400_0deg_test)):

            R_sample_400 = (((n_eff - n_sample) ** 2) / ((n_eff + n_sample) ** 2))
            R_sample_200 = (((n_eff_200 - n_sample) ** 2) / ((n_eff + n_sample) ** 2))

        self.ref_fres_400.append(R_sample)
        self.ref_fres_200.append()

    
    def ref_abs(self, R_ref, I_sample, I_ref):

        for i in range(len(self.scaled_400_test)):

     
    def ref_calibration(self, R_ref, I_sample, I_ref):



    def ref_experiment(self, R_ref, I_sample, I_ref):
            
        I_IL_15_400 = self.scaled_400_test[3][i] - self.scaled_400_test[4][i]
        I_IL_15_200 = self.scaled_200_test[3][i] - self.scaled_200_test[4][i]



anal = Analysis()