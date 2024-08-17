import pandas as pd
import joblib
import streamlit as st
from sklearn.preprocessing import StandardScaler



st.title('Model Deployment using Random Forest Regression')

st.sidebar.header('User Input Parameters')
#season	yr	mnth	hr	holiday	weekday	workingday	weathersit	temp	atemp	hum	windspeed

def user_input_features():
    season = st.sidebar.selectbox('season',('0','1','2','3'))
    yr = st.sidebar.selectbox('year',('1','0'))
    mnth = st.sidebar.selectbox('Month',('0','1','2','3','4','5','6','7','8','9','10','11'))
    hr = st.sidebar.slider('Hour', 1, 24)
    holiday = st.sidebar.selectbox('Holiday', ('0', '1'))
    weekday = st.sidebar.slider('Weekday',0,6)
    workingday = st.sidebar.selectbox('Workingday',('1','0'))
    weathersit = st.sidebar.selectbox('weathersit',('1','0','2','3'))
    temp = st.sidebar.number_input("Insert the temp")
    atemp = st.sidebar.number_input("Insert atemp")
    hum = st.sidebar.number_input('hum')
    windspeed = st.sidebar.number_input('windspeed')
    
    data = {'season':season,
            'yr':yr,
            'mnth': mnth,
            'hr': hr,
            'holiday': holiday,
            'weekday':weekday,
            'workingday':workingday,
            'weathersit':weathersit,
            'temp':temp,
            'atemp':atemp,
            'hum':hum,
            'windspeed':windspeed
            }
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

model=joblib.load(r"C:\Users\Tq28\Bike_rental.py",'rb')
prediction = model.predict(df)
st.subheader('Predicted Result')
st.write(prediction)

