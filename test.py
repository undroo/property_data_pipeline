import os
import pandas as pd
import csv
from population import Population
import streamlit as st

# Interpret data from each census data file
# G01: Total population
file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G01_NSW_POA.csv'

df = pd.read_csv(file_path, header=0)

# Suburb example
kf_df = df.query('POA_CODE_2021 == "POA2220"')
# print(kf_df.head())

population = Population(kf_df)

# Streamlit app
st.title("Mascot Census Data")
# Total population
st.write(population.get_total_population())

# Australian citizen status
st.write(population.get_australian_citizen_status())   

# % of people who are Australian citizens
st.write(population.get_australian_citizen_status()['total'] / population.get_total_population()['total'])

# Age distribution as a % in table
age_distribution = population.get_age_distribution()


# Education attendance
st.write(population.get_education_attendance())


