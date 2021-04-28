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

#tempData['MAGNITUDE'] = tempData['MAGNITUDE'].replace(r'^\s*$', np.nan, regex=True)
#tempData['MAGNITUDE'] = tempData['MAGNITUDE'].astype(float)

#tempData['BEGIN_TIME'].replace(0, np.nan)
#tempData['BEGIN_TIME'] = tempData['BEGIN_TIME'].astype(str)
#tempData['BEGIN_TIME'] = tempData['BEGIN_TIME'].str.zfill(4)

#tempData = tempData.dropna()
tempData.drop(labels = 0, axis = 0, inplace = True)

tempData['Year'] = pd.to_datetime(tempData['Year'], format = '%Y')

tempData['# of Tornados'] = tempData['# of Tornados'].astype(float)


data = pd.DataFrame(tempData[['Year','# of Tornados',]])

#data = data.assign(newtime=pd.to_datetime(data.pop('BEGIN_TIME'), format='%H%M').dt.strftime('%H:%M'))
#data.newtime = pd.to_timedelta(data.newtime+':00')
#data = data.assign(observe_time = data.pop('BEGIN_DATE') + data.pop('newtime'))

data.plot('Year', '# of Tornados', figsize = (10,5))



