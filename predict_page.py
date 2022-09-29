import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        dt = pickle.load(file)
    return dt

dt = load_model()

regressor_loaded = dt['model']
le_country = dt['le_country']
le_gender = dt['le_gender']
le_education = dt['le_education']

def show_predict_page():
    st.title('Software Developer Salary Prediction App')

    st.write('''### Please enter Software Developer detail for the Salary prediction''')

    country = ('UK', 'Netherlands', 'USA', 'Austria', 'Italy', 'Canada', 'Germany', 'Poland', 'France', 'Brazil', 'Sweden', 'Spain', 'Turkey', 'India', 'Russia', 'Switzerland', 'Australia')

    gender = (
        'Man', 
        'Woman'
    )

    education_level = (
        'Master degree', 
        'Bachelor degree', 
        'Under graduate',
        'Post graduate'
    )

    country = st.selectbox('country', country)

    gender = st.selectbox('gender', gender)

    education_level = st.selectbox('education_leve', education_level)

    experience = st.slider('Number of Years of Experience', 0, 50, 2)

    OK = st.button('Calculate Estimated Annual Salary')
    if OK:
        Z = np.array([[country, gender, education_level, experience]])
        Z[:, 0] = le_country.transform(Z[:, 0])
        Z[:, 1] = le_gender.transform(Z[:, 1])
        Z[:, 2] = le_education.transform(Z[:, 2])

        salary = regressor_loaded.predict(Z)

        st.subheader(f'Your Estimated Annual Salary is ${salary[0]:.2f}')


