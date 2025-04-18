import os
import pandas as pd
import csv
from population import Population
import streamlit as st


file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G17C_NSW_POA.csv'

df = pd.read_csv(file_path, header=0)
print(df.head())
for i in df.columns:
    print(i)

