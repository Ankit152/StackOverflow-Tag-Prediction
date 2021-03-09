# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:47:31 2021

@author: ankit
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
ls=[['he','is','a','good','boy'],
    ['he','is','bad']]
nls=[]
for ar in ls:
    s=" "
    s=s.join(ar)
    nls.append(s)
    
print(nls)
#ls=["he is a good boy","he is bad"]
'''
cv=CountVectorizer()
ls=cv.fit_transform(ls)

print(type(ls))'''