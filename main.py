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
    
    gender_dict = {"Male":0,"Female":1,"Non-Binary":2} 
    gender=st.sidebar.radio('Gender',tuple(gender_dict.keys())) 
    st.markdown('''Gender: **:blue[{}]**'''.format(gender))

    age_dict = {"Older than 35":0,"Younger than 35":1} 
    age=st.sidebar.radio('Age',tuple(age_dict.keys())) 
    st.markdown('Age: **:blue[{}]**'''.format(age))

    accessibility_dict = {"No":0,"Yes":1} 
    accessibility=st.sidebar.radio('Any disabilities?',tuple(accessibility_dict.keys())) 
    st.markdown('Accessibility: **:blue[{}]**'''.format(accessibility))

    employment_dict = {"No":0,"Yes":1} 
    employment=st.sidebar.radio('Current Employed?',tuple(employment_dict.keys())) 
    st.markdown('Employment Status: **:blue[{}]**'''.format(employment))

    mental_health_dict = {"No":0,"Yes":1} 
    mental_health=st.sidebar.radio('Mental Health Issues?',tuple(mental_health_dict.keys())) 
    st.markdown('Mental Health: **:blue[{}]**'''.format(mental_health))

    main_branch_dict = {"Non-Developer":0,"Developer":1} 
    main_branch=st.sidebar.radio('Are you a Developer?',tuple(main_branch_dict.keys())) 
    st.markdown('Developer: **:blue[{}]**'''.format(main_branch))

    years_code=st.sidebar. slider('Years of Coding?',0,50,0,)  
    st.markdown('Years of Coding: **:blue[{}]**'''.format(years_code))

    years_code_pro=st.sidebar.slider('Years of Coding Professionally?',0,50,0,)  
    st.markdown('Years of Coding Professionally: **:blue[{}]**'''.format(years_code_pro))

    prev_salary=st.sidebar.number_input('Most Recent Annual Salary?',value=0,step=1)  
    st.markdown('Most Recent Annual Salary: **:blue[{}]**'''.format(prev_salary))

    st.sidebar.markdown('Education Level?') 
    edu_lvl_nohighered=st.sidebar.checkbox('No Higher Education') 
    edu_lvl_undergrad=st.sidebar.checkbox('Undergraduate') 
    edu_lvl_master=st.sidebar.checkbox('Master') 
    edu_lvl_phd=st.sidebar.checkbox('PHD') 
    edu_lvl_other=st.sidebar.checkbox('Other')
    education = []
    if edu_lvl_nohighered:
        education.append('No Higher Education')
    if edu_lvl_undergrad:
        education.append('Undergraduate')  
    if edu_lvl_master:
        education.append('Master')  
    if edu_lvl_phd:
        education.append('PHD')  
    if edu_lvl_other:
        education.append('Other')     
    education = ', '.join(education) 
    st.write('Education Level: **:blue[{}]**'''.format(education))

    tech=st.sidebar.text_area('Technologies (please separate with commas thank you):')
    st.markdown('Technologies: **:blue[{}]**'''.format(tech))

    code_language=st.sidebar.text_area('Coding Languages (please separate with commas thank you):')
    st.markdown('Coding Languages: **:blue[{}]**'''.format(code_language))

    st.subheader('Please confirm the information above before using our prediction model.')
     #if st.button("Predict"):        file_ = open("6m-rain.gif", "rb")        contents = file_.read()        data_url = base64.b64encode(contents).decode("utf-8")        file_.close()        file = open("green-cola-no.gif", "rb")        contents = file.read()        data_url_no = base64.b64encode(contents).decode("utf-8")        file.close()        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))        prediction = loaded_model.predict(single_sample)        if prediction[0] == 0 :            st.error(    'According to our Calculations, you will not get the loan from Bank'    )            st.markdown(    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',    unsafe_allow_html=True,)        elif prediction[0] == 1 :            st.success(    'Congratulations!! you will get the loan from Bank'    )            st.markdown(    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',    unsafe_allow_html=True,    )