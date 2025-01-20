from research_practicum.data_gathering import DataGathering

class Analysis:

    def __init__(self):
        
        filenames = ['calibration', 'beellyfat']
        self.testdata = 
        self.data = DataGathering(filenames[0]) 
        self.abs_ref = []

    def fresnel_reflection(self, n_eff, n_sample):

        return (((n_eff - n_sample) ** 2) / ((n_eff + n_sample) ** 2))
    
    def absolute_reflectance(self, R_ref, I_sample, I_sample_back, I_ref, I_ref_back):

        for i in range(len(self.data.scaled_400)):
            
            I_IL_15_400 = self.data.scaled_400[1][i], self.data.scaled_400[2][i]
            I_IL_15_200 = self.data.scaled_200[1][i] - self.data.scaled_200[2][i]

        self.abs_ref.append(R_ref * ((I_sample - I_sample_back) / (I_ref - I_ref_back)))
    


