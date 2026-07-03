# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
import pandas as pd
import numpy as np

model = pickle.load(open('D:/AI Projects/House Price Prediction/model/house_price_model.sav','rb'))

st.title('House Price prediction')
    
# input the data 
longitude = st.number_input('enter the longitude')  # Float
latitude = st.number_input('enter the latitude')  # Float
housing_median_age =  st.number_input('enter the housing_median_age')  # int
total_rooms =  st.number_input('enter the SkinThickness value')  # int
total_bedrooms =  st.number_input('enter the total_rooms')  # int
population =  st.number_input('enter the Number of population')  # int
households =  st.number_input('enter the Number of households')  # int
median_income = st.number_input('enter the median_income') # Float
ocean_proximity = st.text_input('enter the ocean_proximity') # object


# Make a prediction system

# Maka a button 
if st.button('Predict The Price'):
    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })
    
    Price_pred = np.exp(model.predict(input_data))
    st.success(f"The House Price is: $ {Price_pred[0]:.2f}")

