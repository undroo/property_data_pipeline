import os
import pandas as pd
import csv
from population import Population
import streamlit as st

# Interpret data from each census data file
# G01: Total population
# file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G01_NSW_POA.csv'

# df = pd.read_csv(file_path, header=0)

# # Suburb example
# kf_df = df.query('POA_CODE_2021 == "POA2220"')
# # print(kf_df.head())


# income_file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G37_NSW_POA.csv'

# income_df = pd.read_csv(income_file_path, header=0)
# print(income_df.head()) 
# for i in income_df.columns:
#     print(i)

ancestry_file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G08_NSW_POA.csv'

ancestry_df = pd.read_csv(ancestry_file_path, header=0)
print(ancestry_df.head())
for i in ancestry_df.columns:
    print(i)

