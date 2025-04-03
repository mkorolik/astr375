import os

import numpy as np
import scipy as sp
import pandas as pd

import matplotlib as mpl

import matplotlib.pyplot as plt

from ipywidgets import interact, IntSlider

from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker


import seaborn as sns

import scipy.signal
import scipy.integrate
from scipy.interpolate import make_smoothing_spline

from datetime import datetime
from tomso import gyre

from tqdm import tqdm

print(f'Updated module {datetime.now()}')

plt.rcParams.update({'axes.linewidth' : 1,
                     'ytick.major.width' : 1,
                     'ytick.minor.width' : 1,
                     'xtick.major.width' : 1,
                     'xtick.minor.width' : 1,
                     'xtick.labelsize': 10, 
                     'ytick.labelsize': 10,
                     'axes.labelsize': 12,
                     'font.family': 'Serif',
                      'figure.figsize': (6, 4)
                    })


class model:
    def __init__(self, logs_dir):
        print(f'Creating model from directory {logs_dir}')

        self.logs_dir = logs_dir

        def load_history_file():
            return pd.read_table(os.path.join(self.logs_dir, 'history.data'), 
                skiprows=5, sep=r'\s+')

        def get_index():
            return pd.read_table(os.path.join(self.logs_dir, 'profiles.index'), 
                names=['model_number', 'priority', 'profile_number'],
                skiprows=1, sep=r'\s+')
        
        self.DF = load_history_file()
        self.index = get_index()  
        
        def load_profile(profile_number):
            prof = pd.read_table(
                os.path.join(self.logs_dir, 'profile' + str(profile_number) + '.data'), 
                skiprows=5, sep=r'\s+', engine='c')

        def get_profiles():
            return [load_profile(profile_number) 
                    for profile_number in tqdm(self.index.profile_number)]

        print('Loading Profiles: ')
        self.profs = get_profiles()

    
    def get_value_profile(self, value, prof_num):
        model_num = self.index.iloc[np.argwhere(self.index.profile_number==prof_num)[0][0]].model_number
        df_mod = self.DF.iloc[np.argwhere(self.DF.model_number==model_num)[0][0]]
        return df_mod[value]