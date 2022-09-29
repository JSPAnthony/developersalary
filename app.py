from enum import auto
from tkinter import Image
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from readme import show_readme_page


page = st.sidebar.selectbox('Explore or Predict, ReadMe', ('Predict', 'Explore', 'ReadMe'))

if page == 'Predict':
    show_predict_page()
elif page == 'Explore':
    show_explore_page()
else:
    show_readme_page()


