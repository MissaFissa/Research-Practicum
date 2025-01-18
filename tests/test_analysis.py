from test_data_gathering import DataGathering
from data_gathering import DataExperiment

filenames = ['calibration', 'bellyfat']

calibration = DataGathering(filenames[0])
bellyfat = DataGathering(filenames[1])
bellyfat.effective_index()




