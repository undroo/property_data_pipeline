import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from population import Population

# Set page config
st.set_page_config(
    page_title="Australian Census Data Explorer",
    page_icon="🇦🇺",
    layout="wide"
)

# Load the census data
@st.cache_data
def load_census_data():
    file_path = 'Data/Census/2021_GCP_POA_for_NSW_short-header/2021 Census GCP Postal Areas for NSW/2021Census_G01_NSW_POA.csv'
    return pd.read_csv(file_path, header=0)

# Function to create age distribution chart
def create_age_distribution_chart(age_data):
    l =[]
    for age_group, data in age_data.items():
        l.append({'Age Group': age_group, 'Population': data['total'], 'Gender': 'Total'})
        l.append({'Age Group': age_group, 'Population': data['male'], 'Gender': 'Male'})
        l.append({'Age Group': age_group, 'Population': data['female'], 'Gender': 'Female'})

    
    age_df = pd.DataFrame(l)
    
    fig = px.bar(age_df, x='Age Group', y='Population', color='Gender', barmode='group',
                 title='Population by Age Group and Gender')
    return fig

# Function to create education completion chart
def create_education_completion_chart(education_data):
    edu_df = pd.DataFrame([
        {'Level': level.replace('_', ' ').title(), 'Count': data['total']}
        for level, data in education_data.items()
    ])
    
    fig = px.bar(edu_df, x='Level', y='Count',
                 title='Educational Completion Levels')
    return fig

# Function to create education attendance percentage chart
def create_education_attendance_chart(edu_attendance, age_distribution):
    """Creates a bar chart showing percentage of each age group attending educational institutions"""
    attendance_percentages = []
    
    # Calculate percentages for each age group
    for age_group in ['0-4', '5-14', '15-19', '20-24']:
        total_in_age_group = age_distribution[age_group]['total']
        attending = edu_attendance[age_group]['total']
        if total_in_age_group > 0:  # Avoid division by zero
            percentage = (attending / total_in_age_group) * 100
        else:
            percentage = 0
        
        attendance_percentages.append({
            'Age Group': age_group,
            'Percentage': percentage
        })
    
    # Special handling for 25+ age group (need to sum up all age groups 25 and over)
    total_25_plus = sum(age_distribution[group]['total'] for group in ['25-34', '35-44', '45-54', '55-64', '65-74', '75-84', '85+'])
    attending_25_plus = edu_attendance['25+']['total']
    percentage_25_plus = (attending_25_plus / total_25_plus * 100) if total_25_plus > 0 else 0
    
    attendance_percentages.append({
        'Age Group': '25+',
        'Percentage': percentage_25_plus
    })
    
    # Create DataFrame and plot
    attendance_df = pd.DataFrame(attendance_percentages)
    fig = px.bar(attendance_df, 
                 x='Age Group', 
                 y='Percentage',
                 title='Percentage of Age Group Attending Educational Institutions',
                 labels={'Percentage': 'Percentage Attending (%)'},
                 text=attendance_df['Percentage'].round(1))
    
    # Customize the layout
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(yaxis_range=[0, 100])  # Set y-axis to 0-100%
    
    return fig

# Main app
st.title("🇦🇺 Australian Census Data Explorer")
st.write("Explore demographic data from the 2021 Australian Census by postcode")

# Load data
df = load_census_data()

# Postcode input
postcode = st.text_input("Enter Postcode:", "2000")
if postcode:
    try:
        # Filter data for the selected postcode
        postcode_df = df.query(f'POA_CODE_2021 == "POA{postcode}"')
        
        if not postcode_df.empty:
            population = Population(postcode_df)
            
            # Create columns for layout
            col1, col2 = st.columns(2)
            
            with col1:
                # Total Population Statistics
                st.subheader("📊 Population Overview")
                total_pop = population.get_total_population()
                
                # Create metrics for population
                col1a, col1b, col1c = st.columns(3)
                col1a.metric("Total Population", f"{int(total_pop['total']):,}")
                col1b.metric("Males", f"{int(total_pop['male']):,}")
                col1c.metric("Females", f"{int(total_pop['female']):,}")
                
                # Citizenship
                st.subheader("🏛️ Citizenship")
                citizen_stats = population.get_australian_citizen_status()
                citizen_percentage = (citizen_stats['total'] / total_pop['total']) * 100
                st.metric("Australian Citizens", 
                         f"{int(citizen_stats['total']):,}",
                         f"{citizen_percentage:.1f}% of total population")
                
            with col2:
                # Indigenous Statistics
                st.subheader("🪃 Indigenous Population")
                indigenous_stats = population.get_indigenous_statistics()
                indigenous_total = indigenous_stats['total']['total']
                indigenous_percentage = (indigenous_total / total_pop['total']) * 100
                st.metric("Indigenous Population", 
                         f"{int(indigenous_total):,}",
                         f"{indigenous_percentage:.1f}% of total population")
                
                # Breakdown of Indigenous population
                if indigenous_total > 0:
                    st.write("Indigenous Population Breakdown:")
                    for category in ['aboriginal', 'torres_strait_islander', 'both']:
                        count = indigenous_stats[category]['total']
                        if count > 0:
                            st.write(f"- {category.replace('_', ' ').title()}: {int(count):,}")
            
            # Age Distribution
            st.subheader("👥 Age Distribution")
            age_dist = population.get_age_distribution()
            print(age_dist)
            age_chart = create_age_distribution_chart(age_dist)
            st.plotly_chart(age_chart, use_container_width=True)
            
            # Education Statistics
            st.subheader("📚 Education")
            
            # Current Education Attendance
            col3, col4 = st.columns(2)
            
            with col3:
                st.write("**Educational Institution Attendance by Age Group**")
                edu_attendance = population.get_education_attendance()
                age_dist = population.get_age_distribution()
                attendance_chart = create_education_attendance_chart(edu_attendance, age_dist)
                st.plotly_chart(attendance_chart, use_container_width=True)
            
            with col4:
                st.write("**Highest Level of Education Completed**")
                edu_completion = population.get_education_completion()
                completion_chart = create_education_completion_chart(edu_completion)
                st.plotly_chart(completion_chart, use_container_width=True)
                
        else:
            st.error(f"No data found for postcode {postcode}")
            
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
else:
    st.info("Please enter a postcode to view census data")
