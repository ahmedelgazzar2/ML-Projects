# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:40:15 2026

@author: Dell
"""

import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# load the three models

diabetic_model = pickle.load(open('D:/AI Projects/Multi Diseases Prediction/Models/Diabatic_prediction_model.sav','rb'))

heart_model = pickle.load(open('D:/AI Projects/Multi Diseases Prediction/Models/heart_disease_prediction_model.sav','rb'))

parkinson_model = pickle.load(open('D:/AI Projects/Multi Diseases Prediction/Models/Parkinsons_Disease_prediction_model.sav','rb'))

# load the diabetic scaler

diabetic_scaler = pickle.load(open('D:/AI Projects/Multi Diseases Prediction/Models/scaler.sav','rb'))

# Navigate the side bar
with st.sidebar:
    
    selected = option_menu(
                    menu_title="Multiple Disease Prediction using ML",
                    menu_icon='hospital',
                    options=[
                        "Diabetes Prediction",
                        "Heart Disease Prediction",
                        "Parkinsons Disease Prediction"
                    ],
                    icons=["activity", "heart", "person"],
                    default_index=0)
    
# build the prediction page

# diabatic page
if selected == 'Diabetes Prediction':
    # page title
    st.title('Diabatic prediction')
    
    # input the data 
    Pregnancies = st.text_input('enter the Number of Pregnancies')
    Glucose = st.text_input('enter Glucose Level')
    BloodPressure = st.text_input('enter the BloodPressure value')
    SkinThickness = st.text_input('enter the SkinThickness value')
    Insulin = st.text_input('enter the Insulin Level')
    BMI = st.text_input('enter the BMI Level')
    DiabetesPedigreeFunction = st.text_input('enter the DiabetesPedigreeFunction Level')
    Age = st.text_input('enter the Age')
    
    # Make a prediction system
    
    # Maka a button 
    if st.button('test the diabetes'):
        input_data = list(map(float,[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]))
        diab_pred = diabetic_model.predict_proba([input_data])
        if diab_pred[0][1] > 0.4:
            st.error("The person is diabetic")
        else:
            st.success("The person is not diabetic")

 
# Heart disease page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease prediction')
    
    # input the data 
    age = st.text_input('enter your age')
    sex = st.text_input('enter your gender')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Make a prediction system
    input_data = list(map(float,[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]))
    
    # Maka a button 
    if st.button('test the heart disease'):
        heart_pred = heart_model.predict([input_data])
        if heart_pred[0] == 1:
            st.error("The person has a heart disease")
        else:
            st.success("The person hasn't a heart disease")
 
    
#Parkinsons Disease page
if selected == 'Parkinsons Disease Prediction':
    # page title
    st.title('Parkinsons Disease page')   
    
    # input the data 
    fo = st.text_input('MDVP:Fo(Hz)')
    fhi = st.text_input('MDVP:Fhi(Hz)')  
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
    
    # Make a prediction system
    input_data = list(map(float,[fo, fhi, flo, Jitter_percent, Jitter_Abs,
                                 RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                                 APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]))
    
    # Maka a button 
    if st.button('test the Parkinsons Disease'):
        parkinson_model = parkinson_model.predict([input_data])
        if parkinson_model[0] == 1:
            st.error("The person has Parkinsons Disease")
        else:
            st.success("The person hasn't Parkinsons Disease")
    
    
    
    
    
    