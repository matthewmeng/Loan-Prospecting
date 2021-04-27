import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import warnings
import gc
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
# %matplotlib inline

start_df = pd.read_excel('Sample_data_approved.xls')

df = start_df.copy(deep=True)

# print(df.head())

print(df.shape)