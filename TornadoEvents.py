# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:28:05 2021

@author: Stel
"""

import numpy as np
import pandas as pd 
import datetime as dt


file = "MichiganTornados.csv"

tempData = pd.read_csv(file, error_bad_lines=False)

tempData.drop(labels = 0, axis = 0, inplace = True)

tempData['Year'] = pd.to_datetime(tempData['Year'], format = '%Y')

tempData['# of Tornados'] = tempData['# of Tornados'].astype(float)


data = pd.DataFrame(tempData[['Year','# of Tornados',]])

data.plot('Year', '# of Tornados', figsize = (10,5))




