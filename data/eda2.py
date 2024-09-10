#%% Importing Libraries
import pandas as pd

import os
print(os.getcwd())

#%% Importing dataframes

acidentes_df = pd.read_csv('/raw/datatran2023.csv', sep=';')
# %%