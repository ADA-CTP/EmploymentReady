import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import load
from employment import Model_Input, UNEMPLOYMENTMODEL

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


app_mode = st.sidebar.selectbox('Select Page',['Job Applicants Dataset','Prediction Model']) #two pages

if app_mode == 'Job Applicants Dataset':
    st.checkbox("Use container width", value=False, key="use_container_width")
    st.dataframe(df,use_container_width=st.session_state.use_container_width)
    st.dataframe(hold, use_container_width=st.session_state.use_container_width)
elif app_mode == 'Prediction Model':   
    st.subheader('Please enter all necessary informations to calculate your employability as a Software Developer!')    
    st.sidebar.header("Input your information here:")    
    
    gender_dict = {"Male":0,"Female":1,"Non-Binary":2} 
    gender=st.sidebar.radio('Gender',tuple(gender_dict.keys())) 
    st.markdown(f'Gender: **:blue[{gender}]**')
    gender = gender_dict[gender]

    age_dict = {"Older than 35":0,"Younger than 35":1} 
    age=st.sidebar.radio('Age',tuple(age_dict.keys())) 
    st.markdown(f'Age: **:blue[{age}]**')
    age = age_dict[age]

    accessibility_dict = {"No":0,"Yes":1} 
    accessibility=st.sidebar.radio('Any disabilities?',tuple(accessibility_dict.keys())) 
    st.markdown(f'Accessibility: **:blue[{accessibility}]**')
    accessibility = accessibility_dict[accessibility]

    employment_dict = {"No":0,"Yes":1} 
    employment=st.sidebar.radio('Current Employed?',tuple(employment_dict.keys())) 
    st.markdown(f'Employment Status: **:blue[{employment}]**')
    employment = employment_dict[employment]

    mental_health_dict = {"No":0,"Yes":1} 
    mental_health=st.sidebar.radio('Mental Health Issues?',tuple(mental_health_dict.keys())) 
    st.markdown(f'Mental Health: **:blue[{mental_health}]**')
    mental_health = mental_health_dict[mental_health]

    main_branch_dict = {"Non-Developer":0,"Developer":1} 
    main_branch=st.sidebar.radio('Are you a Developer?',tuple(main_branch_dict.keys())) 
    st.markdown(f'Developer: **:blue[{main_branch}]**')
    main_branch = main_branch_dict[main_branch]

    years_code=st.sidebar. slider('Years of Coding?',0,50,0,)  
    st.markdown(f'Years of Coding: **:blue[{years_code}]**')

    years_code_pro=st.sidebar.slider('Years of Coding Professionally?',0,50,0,)  
    st.markdown(f'Years of Coding Professionally: **:blue[{years_code_pro}]**')

    prev_salary=st.sidebar.number_input('Most Recent Annual Salary?',value=0,step=1)  
    st.markdown(f'Most Recent Annual Salary: **:blue[{prev_salary}]**')

    ed_level_dict = {'No Higher Education':'edlevel_nohighered','Undergraduate':'edlevel_other','Master':'edlevel_master','PHD':'edlevel_phd','Other':'edlevel_other'} 
    education=st.sidebar.radio('Highest Employment Level?',tuple(ed_level_dict.keys())) 
    st.markdown(f'Highest Education Level: **:blue[{education}]**')
    education = ed_level_dict[education]

    tech=st.sidebar.text_area('Technologies & Coding Languages (please separate with commas thank you):')
    st.markdown(f'Technologies & Coding Languages: **:blue[{tech}]**')

    st.subheader('Please confirm the information above before using our prediction model.')
    # feature_list = [gender,age,accessibility,employment,mental_health,main_branch,years_code,years_code_pro,prev_salary,education,tech]
    # st.write(feature_list)

    if st.button("PREDICT"):        
        user_input_1 = Model_Input(gender,age,accessibility,employment,mental_health,main_branch,years_code,years_code_pro,prev_salary,education,tech).run()        
        prediction_model_1 = UNEMPLOYMENTMODEL('./model/gradientboost.joblib',user_input_1)
        st.markdown(f'**:violet[{prediction_model_1.predict()}]**')
        st.markdown(f'Chance of Being Employed: **:violet[{prediction_model_1.proba()*100:.2f}%]**')
        proba_1 = prediction_model_1.proba()
        st.markdown(f'Recommended Skills to Improve Employability: **:violet[{prediction_model_1.recommend_skills()}]**')
        
        # if st.button("UPDATE"):        
        #     user_input_2 = Model_Input(gender,age,accessibility,employment,mental_health,main_branch,years_code,years_code_pro,prev_salary,education,tech).run()        
        #     st.markdown(f'**:violet[{prediction_model_1.improvement_prediction(user_input_2)}]**')
        #     st.markdown(f'Recommended Skills to Improve Employability: **:violet[{prediction_model_1.model.improvement_recommend_skills()}]**')

