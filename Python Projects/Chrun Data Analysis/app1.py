import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fetching Data 
df  = pd.read_csv(r'E:\Croma\Projects\Python Projects\Chrun Data Analysis\Datasets\Churn_Modelling.csv')

# Web Application's Page Configuration
st.set_page_config(layout='wide' , page_title="Churn Analysis " )

#Copy a dataset 
newdf = df.copy()
newdf = newdf.rename(columns={'Geography' : 'Country'})

col1 , col2, col3, col4 , col5= st.columns(5)
with col1:
  country  = st.selectbox("Select Country", ['All'] + list(newdf['Country'].unique()))
  if country!='All':
   newdf =  newdf[newdf['Country']==country]
with col2:
  gender = st.selectbox("Select Gender" , ['All'] + list(newdf['Gender'].unique()))
  if gender!='All':
    newdf = newdf[newdf['Gender']==gender]
with col3:
  newdf['IsActiveMember']=newdf['IsActiveMember'].replace({0:'In_Active' , 1:'Active'})
  status = st.selectbox('Select Active Status',['All'] + list(newdf['IsActiveMember'].unique()))
  if status!='All':
    newdf = newdf[newdf['IsActiveMember']==status]
with col4:
  newdf['HasCrCard'] = newdf['HasCrCard'].replace({0:'Available' , 1:'Not_Available'})
  status = st.selectbox('HasCrCard',['All'] + list(newdf['HasCrCard'].unique()))
  if status!='All':
    newdf = newdf[newdf['HasCrCard']==status]
with col5:
  newdf['Exited'] = newdf['Exited'].replace({0:'Stay connected',1:'Exited'})
  exited = st.selectbox('Is_Exited' ,['All'] + list(newdf['Exited'].unique()))
  if exited!='All':
    newdf = newdf[newdf['Exited']==exited]

#KPIs Key Point Indicators
col1 , col2 , col3 ,  col4 , col5 = st.columns(5)

with col1:
  st.metric('Total Balance :' , newdf['Balance'].sum().round(2))
with col2:
  st.metric('Average Credit Score : ', newdf['CreditScore'].mean().round(2))
with col3:
  st.metric('Total Salary :' , newdf['EstimatedSalary'].sum().round(2))
with col4:
  st.metric('Average Salary : ' , newdf['EstimatedSalary'].mean().round(2))
with col5:
  st.metric('Total No. of Customers : ' , newdf.shape[0])

#Trend and Insight charts
# column = st.selectbox('Select data', newdf.drop(columns='Surname').select_dtypes(include='str').columns)             # ise dynamic kaise bnay

# col1 , col2 , col3 , col4= st.columns(4)
# with col1:
#     fig, ax = plt.subplots(figsize=(5,3))
#     sns.histplot(data=newdf, x='Age', kde=True, ax=ax)
#     ax.set_title("Age Distribution")
#     st.pyplot(fig)
# with col2:
#     fig , ax = plt.subplots(figsize = (5,3.4))
#     sns.histplot(x = 'CreditScore' ,  data =newdf , kde = True)
#     st.pyplot(fig)
# with col3:
#     fig, ax = plt.subplots(figsize=(6,4))
#     sns.boxplot(data=newdf, y='EstimatedSalary', ax=ax)
#     ax.set_title("Salary Boxplot")
#     st.pyplot(fig)
# with col4:
#   fig, ax = plt.subplots(figsize=(5,3))
#   ax.pie(newdf['Gender'].value_counts(),labels=newdf['Gender'].value_counts().index,autopct='%1.1f%%')
#   st.pyplot(fig)




#Sample Dataset View
st.dataframe(newdf , height=250)
st.text(f"Dataset Shape :   {newdf.shape}")


