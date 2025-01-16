from data_gathering import DataGathering

data = DataGathering()

data.background_correction()
data.scale()
data.sellmeier()
data.effective_index()

print(data.dict_experiment)