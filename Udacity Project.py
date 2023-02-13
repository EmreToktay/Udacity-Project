# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 03:00:55 2023

@author: Memre
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data for each year
df_2022 = pd.read_csv("C:/Udacity/Blogspot/2022/survey_results_public.csv")
df_2021 = pd.read_csv("C:/Udacity/Blogspot/2021/survey_results_public.csv")
df_2020 = pd.read_csv("C:/Udacity/Blogspot/2020/survey_results_public.csv")

# Filter for data scientists in Turkey
turkey_programming_2022 = df_2022[(df_2022['Country'] == 'Turkey') &
                                  df_2022['DevType'].str.contains('Data scientist or machine learning specialist')].dropna(subset=['LanguageHaveWorkedWith'])

turkey_programming_2021 = df_2021[(df_2021['Country'] == 'Turkey') &
                                  df_2021['DevType'].str.contains('Data scientist or machine learning specialist')].dropna(subset=['LanguageHaveWorkedWith'])

turkey_programming_2020 = df_2020[(df_2020['Country'] == 'Turkey') &
                                  df_2020['DevType'].str.contains('Data scientist or machine learning specialist')].dropna(subset=['LanguageHaveWorkedWith'])

# Split the data in the "LanguageHaveWorkedWith" column
turkey_programming_2022['LanguageHaveWorkedWith'] = turkey_programming_2022['LanguageHaveWorkedWith'].str.split(
    ";")
turkey_programming_2021['LanguageHaveWorkedWith'] = turkey_programming_2021['LanguageHaveWorkedWith'].str.split(
    ";")
turkey_programming_2020['LanguageHaveWorkedWith'] = turkey_programming_2020['LanguageHaveWorkedWith'].str.split(
    ";")

# Create a dataframe with only the programming languages and their count for 2022
programming_2022 = turkey_programming_2022.explode('LanguageHaveWorkedWith').groupby(
    'LanguageHaveWorkedWith').size().reset_index(name='2022')
programming_2022.columns = ['LanguageHaveWorkedWith', '2022']

# Create a dataframe with only the programming languages and their count for 2021
programming_2021 = turkey_programming_2021.explode('LanguageHaveWorkedWith').groupby(
    'LanguageHaveWorkedWith').size().reset_index(name='2021')
programming_2021.columns = ['LanguageHaveWorkedWith', '2021']

# Create a dataframe with only the programming languages and their count for 2020
programming_2020 = turkey_programming_2020.explode('LanguageHaveWorkedWith').groupby(
    'LanguageHaveWorkedWith').size().reset_index(name='2020')
programming_2020.columns = ['LanguageHaveWorkedWith', '2020']


# Merge the two dataframes
programming = programming_2020.merge(programming_2021, on='LanguageHaveWorkedWith').merge(
    programming_2022, on='LanguageHaveWorkedWith')

# Add a new column with the sum of 2022 and 2021 counts
programming = programming.assign(sum=programming.apply(
    lambda x: x['2022'] + x['2021'] + x['2020'], axis=1)).sort_values(by='sum', ascending=False)

# Display only the top 10 results
top_10 = programming.head(10)

# Plot the bar chart
bar_width = 0.25
x = np.arange(len(top_10))

fig = plt.figure(figsize=(20, 10))

plt.bar(x, top_10['2020'], bar_width, color='green', label='2020')
plt.bar(x + bar_width, top_10['2021'], bar_width, color='blue', label='2021')
plt.bar(x + bar_width * 2, top_10['2022'],
        bar_width, color='orange', label='2022')

# Add labels and title
plt.xticks(x + bar_width, top_10['LanguageHaveWorkedWith'])
plt.xlabel("Programming Language")
plt.ylabel("Count")
plt.title("Top 10 Programming Languages Used by Data Scientists in Turkey (2020 & 2021 & 2022)")

# Add a legend
plt.legend()

# Show the plot
plt.show()
