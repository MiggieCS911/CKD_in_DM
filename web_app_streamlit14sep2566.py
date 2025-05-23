# -*- coding: utf-8 -*-
"""web_app_streamlit14Sep2566.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16SLobNNtytW8GsnE41IwmZojadtw7gIy
"""

###web application: DM, CKD##

#import essential library
import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
# import sklearn

#load model
#xgb
xgbmodel = xgb.XGBClassifier()
xgbmodel.load_model('xgbc_dm_ckd_noHba1c.json')

#function
@st.cache_resource
def fit_xgb(info):
    res = xgbmodel.predict_proba(info)
    return res[0,1]

# """
# variable lists
# 'BMI', 'SBP', 'DBP', 'FBS', 'age', 'Gender', 'duration'
# BMI: Kg/m2
# SBP: mmHg
# DBP: mmHg
# FBS: mg/dL
# age: year
# Gender: 0 = Female, 1 = Male
# duration: months
# """

#start application
st.title('Pedict Probability of CKD in Diabetic Patient')
txt1 = '''To predict probablity of eGFR below than 60 ml/min/1.73m2.'''
st.write(txt1)

####Input###
st.header('Please input values')

gender = st.radio('Gender', ['male','female'])
if gender == 'male':
    gender = 1
else:
    gender = 0

age = st.number_input('Age (years)',
                      min_value = 18,max_value = 100, value =50, step = 1)

bw = st.number_input('Body weight (Kg)',
                     min_value = 25,max_value = 150, value = 50, step = 1)

ht = st.number_input('Height (cm)',
                     min_value = 120,max_value = 200, value = 160, step = 1)

bmi = bw/((ht/100)**2)

sbp = st.number_input('Systolic BP (mmHg)',
                     min_value = 70,max_value = 250, value = 120, step = 1)

dbp = st.number_input('Diastolic BP (mmHg)',
                     min_value = 30,max_value = 120, value = 80, step = 1)

fbs = st.number_input('Fasting blood sugar (mg/dL)',
                     min_value = 50,max_value = 500, value = 140, step = 1)

duration = sbp= st.number_input('Duration of diabetes (month)',
                     min_value = 0,max_value = 70, value = 0, step = 1)

##wrap up data
patient = np.array([[bmi, sbp, dbp, fbs, age, gender, duration]])

#predict
ans = fit_xgb(patient)

#result
if st.button('Calculated', key = 'predict button'):
    st.header('Results')
    # st.subheader('XGBoost model')
    # st.write('Predict AKRT: ', ans_xgb)
    st.write('The probability of chronic kidney disease is', round(ans*100,2), '%')
st.write('----------------------------------------------------------------------------')

# sidebar
# st.sidebar.header('')
# txt2 = ''''''
# st.sidebar.write(txt2)
# st.sidebar.write('Version 1')
st.sidebar.markdown('&copy; 2023 Wanjak Pongsittisak All Rights Reserved')
#table
performance = {'AUC': [0.82,'NR'],
               'sensitivity': [0.74,0.83],
               'specificity': [0.75,0.68],
               'F1-score': [0.74,'NR'],
               'NPV': [0.83,0.87],
               'PPV':[0.63,0.60]}
tab = pd.DataFrame(performance, index=['Cut point: 50%','Cut point 40%'])
st.header('Performance on Test dataset')
st.dataframe(tab)

#thank you
st.header('Credit')
txt3 = '''All code is written by [Python 3.7] (https://www.python.org/). We thank everyone who contributes to all libraries and packages that we used: [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Scikit-learn](https://scikit-learn.org/stable/), [XGBoost](https://xgboost.readthedocs.io/en/latest/), [Matplotlib](https://matplotlib.org/), and [Streamlit](https://streamlit.io/)'''
st.write(txt3)

