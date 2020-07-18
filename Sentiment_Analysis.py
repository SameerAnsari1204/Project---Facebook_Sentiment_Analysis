# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:17:28 2019

@author: Sameer Ansari
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='Sameer_SentimentAnalysis.xlsx'
xl=pd.ExcelFile(file)
dfs=xl.parse(xl.sheet_names[0])  #All my data is stored in 1st column only
dfs=list(dfs)
#print(dfs)

#Sentiment Analysis

sid=SentimentIntensityAnalyzer()
str1="UTC+05:30" # Using pattern to remove date from data
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])