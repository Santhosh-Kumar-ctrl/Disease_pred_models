import os
import pickle
import streamlit as st # type: ignore #web app
from streamlit_option_menu import option_menu # type: ignore
import sklearn
st.set_page_config(page_title="Prediction of Disease Outbreaks", page_icon="🦠", layout="wide", initial_sidebar_state="expanded")
diabetes_model = pickle.load(open(r"C:\Users\Santhosh Kumar\OneDrive\Desktop\disease_out_predict_mod\training_models\diabetes_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Santhosh Kumar\OneDrive\Desktop\disease_out_predict_mod\training_models\parkinsons_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\Santhosh Kumar\OneDrive\Desktop\disease_out_predict_mod\training_models\heart_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu("Prediction of Disease Outbreak Models",['Diabetes Model','Parkinsons Model','Heart Model'],menu_icon='hospital-fill',icons=['capsule','dash-circle-dotted','heart'],default_index=0)

if selected == 'Diabetes Model':
    st.title("Diabetes Prediction Model")
    col1,col2,col3 = st.columns(3)
    with col1:
        pregnancies = st.number_input("Pregnancies",min_value=0,max_value=17)
        glucose = st.number_input("Glucose",min_value=0,max_value=199)
        blood_pressure = st.number_input("Blood Pressure",min_value=0,max_value=122)
    with col2:
        skin_thickness = st.number_input("Skin Thickness",min_value=0,max_value=99)
        insulin = st.number_input("Insulin",min_value=0,max_value=846)
        bmi = st.number_input("BMI",min_value=0,max_value=67)
    with col3:
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function",min_value=0.0,max_value=2.42)
        age = st.number_input("Age",min_value=21,max_value=81)
    if st.button("Predict"):
        input_data = [[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age]]
        prediction = diabetes_model.predict(input_data)
        if prediction == 1:
            st.error("You have Diabetes")
        else:
            st.success("You don't have Diabetes")
        
        
if selected == 'Parkinsons Model':
    st.title("Parkinsons Prediction Model")
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        MDVP_Fo = st.number_input("MDVP:Fo(Hz)")
        MDVP_Fhi = st.number_input("MDVP:Fhi(Hz)")
        MDVP_Jitter_Abs = st.number_input("MDVP:Jitter(Abs)")
        MDVP_Flo = st.number_input("MDVP:Flo(Hz)")
    with col2:
        MDVP_Jitter = st.number_input("MDVP:Jitter(%)")
        MDVP_Shimmer = st.number_input("MDVP:Shimmer")
        NHR = st.number_input("NHR")
        MDVP_RAP = st.number_input("MDVP:RAP")
    with col3:
        HNR = st.number_input("HNR")
        RPDE = st.number_input("RPDE")
        DFA = st.number_input("DFA")
        MDVP_PPQ = st.number_input("MDVP:PPQ")
    with col4:
        spread1 = st.number_input("spread1")
        spread2 = st.number_input("spread2")
        D2 = st.number_input("D2")
        Shimmer_DDA = st.number_input("Shimmer:DDA")
        PPE = st.number_input("PPE")
    with col5:
        Jitter_DDP = st.number_input("Jitter:DDP")
        MDVP_Shimmer_Db = st.number_input("MDVP:Shimmer(dB)")
        Shimmer_APQ3 = st.number_input("Shimmer:APQ3")
        Shimmer_APQ5 = st.number_input("Shimmer:APQ5")
        MDVP_APQ = st.number_input("MDVP:APQ")
        
    
    if st.button("Predict"):
        input_data = [[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter_Abs,MDVP_Jitter,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_Db,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]]
        prediction = parkinsons_model.predict(input_data)
        if prediction == 1:
            st.error("You have Parkinsons")
        else:
            st.success("You don't have Parkinsons")
            
            
if selected == "Heart Model":
    st.title("Heart Disease Prediction Model")
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.number_input("Age")
        sex = st.selectbox("Gender",["Male","Female"])
        cp = st.number_input("Cp")
        oldpeak = st.number_input("Oldpeak")
    with col2:
        trestbps = st.number_input("Trestbps")
        chol = st.number_input("Thol")
        fbs = st.number_input("Fbs")
        slope = st.number_input("Slope")
    with col3:
        restecg = st.number_input("Restecg")
        thalach = st.number_input("Thalach")
        exang = st.number_input("Exang")
        ca = st.number_input("Ca")
        thal = st.number_input("Thal")
    
    if st.button("Predict"):
        if sex == "Male":
            sex = 1
        else:
            sex = 0
        #sex=1 if sex == "Male" else 0
        input_data = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
        prediction = heart_model.predict(input_data)
        if prediction == 1:
            st.error("You Have Heart Disease")
        else:
            st.success("You Don't Have Heart Disease")