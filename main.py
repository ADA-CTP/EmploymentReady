import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

st.checkbox("Use container width", value=False, key="use_container_width")

st.dataframe(df,use_container_width=st.session_state.use_container_width)

hold = df.copy()
hold = pd.get_dummies(hold,columns=['EdLevel'],drop_first=False)
hold = hold.drop('HaveWorkedWith', axis=1).join(df['HaveWorkedWith'].str.get_dummies(sep=';'))

st.dataframe(hold, use_container_width=st.session_state.use_container_width)