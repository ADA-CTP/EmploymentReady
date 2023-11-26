import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle  

df = pd.read_csv("jobapplicants.csv")
sns.set()
df = df.rename(columns={'Unnamed: 0' : 'id', 'Age':'<35'})
df.replace(('Yes','No'), (1,0), inplace=True)

# Man = 0, Woman = 1, NonBinary = 2
df['Gender'].replace(('Man', 'Woman', 'NonBinary'),(0,1,2),inplace=True)

# NotDev = 0, Dev = 1
df['MainBranch'].replace(('NotDev','Dev'),(0,1), inplace=True)

# >35 = 0, <35 = 1
df['<35'].replace(('>35','<35'), (0,1),inplace=True)

hold = df.copy()
hold = pd.get_dummies(hold,columns=['EdLevel'],drop_first=False)
hold = hold.drop('HaveWorkedWith', axis=1).join(df['HaveWorkedWith'].str.get_dummies(sep=';'))


# testing out widgets for sidebar menu
@st.cache(suppress_st_warning=True)
def get_fvalue(val):    
    feature_dict = {"No":1,"Yes":2}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode == 'Home':
    st.checkbox("Use container width", value=False, key="use_container_width")
    st.dataframe(df,use_container_width=st.session_state.use_container_width)
    st.dataframe(hold, use_container_width=st.session_state.use_container_width)
elif app_mode == 'Prediction':   
    st.subheader('Please enter all necessary informations to calculate your employability as a Software Developer!')    
    st.sidebar.header("Input your information here:")    
    #gender=0, age=0, accessibility=0, employment=0, mental_health=0, main_branch=0, years_code=0, years_code_pro=0, previous_salary=0, education='', tools=
    gender_dict = {"Male":0,"Female":1,"Non-Binary":2} 
    gender=st.sidebar.radio('Gender',tuple(gender_dict.keys())) 
    st.markdown('Gender: '+str(gender))

    age_dict = {"Older than 35":0,"Younger than 35":1} 
    age=st.sidebar.radio('Age',tuple(age_dict.keys())) 
    st.markdown('Age: '+str(age))

    accessibility_dict = {"No":0,"Yes":1} 
    accessibility=st.sidebar.radio('Accessibility',tuple(age_dict.keys())) 
    st.markdown('Accessibility: '+str(accessibility))

    # feature_dict = {"No":1,"Yes":2}    
    # edu={'Graduate':1,'Not Graduate':2}    
    # prop={'Rural':1,'Urban':2,'Semiurban':3}    
    # ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)    
    # CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)    
    # LoanAmount=st.sidebar.slider('LoanAmount in K$',9.0,700.0,200.0)    
    # Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))    
    # Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))    
       
    # Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))    
    # Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))    
    # Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])    
    # Education=st.sidebar.radio('Education',tuple(edu.keys()))    
    # Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))    
    # class_0, class_3, class_1, class_2 = 0,0,0,0    
    # if Dependents == '0':        
    #     class_0 = 1    
    # elif Dependents == '1':        
    #     class_1 = 1    
    # elif Dependents == '2' :        
    #     class_2 = 1    
    # else:        
    #     class_3= 1    
    # Rural,Urban,Semiurban=0,0,0    
    # if Property_Area == 'Urban' :        
    #     Urban = 1    
    # elif Property_Area == 'Semiurban' :        
    #     Semiurban = 1    
    # else :        
    #     Rural = 1