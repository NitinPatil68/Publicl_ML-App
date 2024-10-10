#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 00:06:44 2024

@author: nitinpatil
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Open the model file in binary mode
with open(open('heart_disease_model.sav', 'rb')) as file:
    heart_model = pickle.load(file)

with open(open('diabetes_model.sav', 'rb')) as file:
    Diabetes_model = pickle.load(file)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Heart Disease Prediction',
                                                                  'Diabetes Disease Prediction'], default_index=0)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Collect user input, these will be strings initially
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholesterol in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic Results (values 0,1,2)')
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST Depression Induced by Exercise')
    slope = st.text_input('Slope of Peak Exercise ST Segment')
    ca = st.text_input('Number of Major Vessels Colored by Flouroscopy')
    thal = st.text_input('Thal (0 = normal, 1 = fixed defect, 2 = reversible defect)')

    # Initialize prediction output variable
    heart_diagnosis = ''

    # Create a button for prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to numeric (float or int based on your model's requirements)
            age = int(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = int(trestbps)
            chol = int(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = int(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)  # oldpeak might be a decimal value
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            
            # Make prediction using the model
            Heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
            if Heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'
            else:
                heart_diagnosis = 'The person has a healthy heart'
            
            st.success(heart_diagnosis)
            
        except ValueError:
            st.error('Please ensure all inputs are valid numeric values.')
        
    


if selected == 'Diabetes Disease Prediction':
    st.title('Diabetes Disease Prediction using ML')

    # Collect user input, these will be strings initially
    Pregnancies = st.text_input('Pregnancies')
    Glucose = st.text_input('Glucose')
    BloodPressure = st.text_input('BloodPressure')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    Age = st.text_input('Age')
    
    # Initialize prediction output variable
    Diabetes_diagnosis = ''

    # Create a button for prediction
    if st.button('Diabetes Disease Test Result'):
        try:
            # Convert inputs to numeric (float or int based on your model's requirements)
            Pregnancies = int(Pregnancies)
            Glucose = int(Glucose)
            BloodPressure = int(BloodPressure)
            SkinThickness = int(SkinThickness)
            Insulin = int(Insulin)
            BMI = float(BMI)
            DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
            Age = int(Age)

            
            # Make prediction using the model
            Diabetes_prediction = Diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if Diabetes_prediction[0] == 1:
                Diabetes_diagnosis = 'The person has Diabetes'
            else:
                Diabetes_diagnosis = 'The person has No Diabetes'
            
            st.success(Diabetes_diagnosis)
            
        except ValueError:
            st.error('Please ensure all inputs are valid numeric values.')
        


    



    
