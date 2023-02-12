# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 01:59:30 2023

@author: deniz.toktay
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("D:/Udacity/Blogspot/survey_results_public.csv")

df = df[(df["Country"] == "Turkey") & (df["DevType"].str.contains("Data scientist or machine learning specialist"))]

df = df[["Knowledge1", "Knowledge2", "Knowledge3", "Knowledge4", "Knowledge5", "Knowledge6", "Knowledge7"]]

df = df.dropna(how='all', axis=0)

print(df)

for column in df.columns:
    df[column].value_counts().plot(kind='bar')
    plt.title(column)
    plt.show()
