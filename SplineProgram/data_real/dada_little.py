#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:10:18 2018

@author: semion
"""

import pandas as pd
import numpy as np
import os


file = os.path.abspath("t_p_63_17.csv")

Data = pd.read_csv("t_p_63_17.csv", sep="\t")
tNotNoneData = Data[Data.t_mean != u'None']
preNotNoneData = Data[Data.pre != u'None']
x = tNotNoneData.number.values
y = np.array(tNotNoneData.t_mean.values, dtype=float)

x = x[:1000]
y = y[:1000]
