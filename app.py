import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load('random_forest_health.pkl')
model_columns = joblib.load('columns.pkl')

st.set_page_config(page_title="Teen Mental Health Predicator 🧠",layout="centered",page_icon="🧠")

st.title("Teen Mental Health Predicator 🧠")
st.write("Enter the details below to analyze mental health issues")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age",min_value=10,max_value=25,value=18)
    gender = st.selectbox("Gender", options=[("Male",0),("Female",1)],format_func=lambda x: x[0])[1]
    sleep_hours = st.slider("sleep Hours", 0,12,7)
    physical_activity = st.slider("Physical Activity (1-10)",1,10,5)
    
    with col2:
        academic = st.slider("Academic Performance (1-10)", 1,10,5)
        stress = st.slider("Stress Level (1-10)",1,10,5)
        anxiety = st.slider("Anxiety level(1-10)",1,10,5)
        addiction = st.slider("Addiction level(1-10)",1,10,5)
        
        st.divider()
        st.subheader("Digital Lifestyle")
        social_media_hrs = st.number_input("Daily social media hours",0,24,3)
        screen_time = st.number_input("screen time Before sleep(min)",0,300,30)
        
        platform =st.selectbox("Primary Platform usage",['Instagram','TikTok',"Both"])
        interaction = st.selectbox("Social Interaction level",['Low','Medium','Height'])
        
        if st.button("Predict Mental Health Status"):
            
            input_data = pd.DataFrame(0, index=[0],columns=model_columns)
            
            input_data['age']= age
            input_data['gender']=gender
            input_data['daily_social_media_hours']= social_media_hrs
            input_data['sleep_hours']= sleep_hours
            input_data['screen_time_before_sleep']= screen_time
            input_data['academic_performance'] = academic
            input_data['physical_activity']= physical_activity
            input_data['stress_level']= stress
            input_data['anxiety_level']= anxiety
            input_data['addiction_level']= addiction
            
            if f"platfrom_usage_{platform}" in model_columns:
                input_data[f"platfrom_usage_{platform}"]=1
            
            if f"social_interaction_{interaction.lower()}" in model_columns:
                input_data[f"social_interaction_level_{interaction.lower()}"] = 1
                
            
            prediction = model.predict(input_data)
            
            st.divider()
            if prediction[0] ==1:
                st.error("Result: High Risk of Depression/Mental Health Issues")
                st.write("Recommendation:It is advised to speak with a counselor or a tre")
                
            else:
                st.success("Result: Normal/Low risk")
                st.write("Everything looks good! Maintain a healthy lifestyle")