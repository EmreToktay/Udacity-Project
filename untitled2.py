# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 06:07:39 2023

@author: deniz.toktay
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import scipy.stats as stats

# Reading the csv file into a DataFrame
df_2022 = pd.read_csv("D:/Udacity/Blogspot/2022/survey_results_public.csv")

# Filtering the data for only Turkish developers who are employed full-time and using TRY (Turkish Lira) as their currency
turkey_programming_2022 = df_2022[(df_2022['Country'] == 'Turkey') &
                                  (df_2022['MainBranch'] == 'I am a developer by profession') &
                                  (df_2022['Employment'].str.contains('Employed, full-time')) &
                                  (df_2022['Currency'].str.contains('TRY	Turkish lira'))]

# Removing the rows that have "Just me - I am a freelancer, sole proprietor, etc." as their organization size
turkey_programming_2022 = turkey_programming_2022[turkey_programming_2022['OrgSize']
                                                  != 'Just me - I am a freelancer, sole proprietor, etc.']

# Dropping the rows with missing values in 'CompTotal' column
turkey_programming_2022 = turkey_programming_2022.dropna(subset=['CompTotal'])

# Removing the rows with 'CompTotal' less than 7500
turkey_programming_2022 = turkey_programming_2022[turkey_programming_2022['CompTotal'] >= 7500]

# Removing the rows with 'ConvertedCompYearly' less than 5000
turkey_programming_2022 = turkey_programming_2022[turkey_programming_2022['ConvertedCompYearly'] >= 5000]

# Categories of organization size
org_size_categories = ['2 to 9 employees', '10 to 19 employees', '20 to 99 employees', '100 to 499 employees',
                       '500 to 999 employees', '1,000 to 4,999 employees', '5,000 to 9,999 employees', '10,000 or more employees']

# Calculating the mean salary for each category of organization size
comp_means = []
for size in org_size_categories:
    comp_means.append(round(
        turkey_programming_2022[turkey_programming_2022['OrgSize'] == size]['ConvertedCompYearly'].mean()))

# Creating a DataFrame to store the mean salary for each category of organization size
org_size_comp_mean = pd.DataFrame(
    {'Organization Size': org_size_categories, 'Mean Salary': comp_means})

# Printing the DataFrame
print(org_size_comp_mean)


# Calculate the descriptive statistics for the salary data
salary_data = []
for size in org_size_categories:
    salary_data.append(turkey_programming_2022[turkey_programming_2022['OrgSize'] == size]['ConvertedCompYearly'])
    
# Descriptive Statistics
for i, data in enumerate(salary_data):
    print("\n")
    print("Organization Size: ", org_size_categories[i])
    print("Mean: ", round(data.mean(), 2))
    print("Median: ", round(data.median()))
    print("Standard Deviation: ", round(data.std(), 2))
    print("Minimum: ", round(data.min()))
    print("Maximum: ", round(data.max()))

