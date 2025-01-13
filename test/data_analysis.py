import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from pathlib import Path

cwd = Path.cwd()
df = pd.read_csv(f'{cwd}/data_csv/12_measurements_400mu.csv', sep = 'del', header = None)
print(df)