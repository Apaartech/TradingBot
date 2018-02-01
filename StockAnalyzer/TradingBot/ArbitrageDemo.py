'''
Created on Jan 11, 2018

@author: AH0109019
'''

import numpy as np
import pandas as pd


'Read NSE data'
spot_data = pd.read_csv("C:\\Nilesh\\Apaar\\Trading bot\\cm11JAN2018bhav.csv")
der_data = pd.read_csv("C:\\Nilesh\\Apaar\\Trading bot\\fo11JAN2018bhav.csv")


'Join data sets and based on SYMBOL'
''

arbitrage_input = pd.merge(spot_data,der_data,how='inner', on  = ["SYMBOL"],suffixes=('_spot', '_fut'))

print(arbitrage_input.head())