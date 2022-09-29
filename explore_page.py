import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def group_category(category, cutoff):
    categorical_map = {}
    for i in range(len(category)):
        if category.values[i] >= cutoff:
            categorical_map[category.index[i]] = category.index[i]
        else:
            categorical_map[category.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor degree'
    if 'Master’s degree' in x:
        return 'Master degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post graduate'
    return 'Under graduate'

def clean_gender(x):
    if 'Man' in x:
        return 'Man'
    if 'Woman' in x:
        return 'Woman'
    return 'Other'

@st.cache
def load_dataset():
    df = pd.read_csv('developer_salary_survey_22.csv')
    df = df[df['salary'].notnull()]
    df = df.dropna()
    df.reset_index(drop=True)

    country_map = group_category(df.country.value_counts(), 400)
    df['country'] = df['country'].map(country_map)
    df = df[df["salary"] <= 250000]
    df = df[df["salary"] >= 10000]
    df = df[df['country'] != 'Other']
    df['experience'] = df['experience'].apply(clean_experience)
    df['education_level'] = df['education_level'].apply(clean_education)
    df['country'] = df['country'].replace(['United Kingdom of Great Britain and Northern Ireland', 
                                        'United States of America', 'Russian Federation'],
                                        ['UK', 'USA', 'Russia'])
    df['gender'] = df['gender'].apply(clean_gender)
    df = df[df['gender'] != 'Other']
    df.reset_index(drop=True)

    return df

df = load_dataset()

def show_explore_page():
    st.title('Exploring Software Developer Salaries Year 2022')

    st.write(
        '''
        ### Dataset from Stack Overflow Developer 2022 Survey
        https://insights.stackoverflow.com/survey
        '''
    )

    data = df['country'].value_counts()
    
    fig1, axe1 = plt.subplots()
    axe1.pie(data, labels=data.index, autopct='%1.1f%%', shadow=True, startangle=90)
    axe1.axis('equal')

    st.write('''### Data from Different Countries''')

    st.pyplot(fig1)

    st.write('''### Mean Salary by Country''')

    dt = df.groupby(['country'])['salary'].mean().sort_values(ascending=True)
    st.bar_chart(dt)

    st.write('''### Mean Salary by Experience''')

    my_data = df.groupby(['experience'])['salary'].mean().sort_values(ascending=True)
    st.line_chart(my_data)
    



    
