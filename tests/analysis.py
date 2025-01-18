from data_gathering import DataCalibration, DataExperiment

data = DataCalibration()

data.split_dataframe()
data.background_correction()
data.scale()
data.sellmeier()
data.effective_index()

