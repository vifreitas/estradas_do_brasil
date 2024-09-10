#%% Importing Libraries
import pandas as pd

#%% Importing dataframe

root_folder = 'D:/Projetos Data Science/estradas_do_brasil'
acidentes_df = pd.read_csv(f'{root_folder}/data/raw/datatran2023.csv', sep=';', encoding='ANSI')

# %%

