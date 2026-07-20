import pandas as pd 
import streamlit as st

#Web Application's page Configuration
st.set_page_config(layout='wide' , page_title='Sales Analysis')

#Header
st.title('Sales Dataset Analysis')

# load dataset 
df = pd.read_excel('dataset/Financial_Sample.xlsx')

# Handle Missing Values
for col in df.columns:
  if df[col].isnull().sum()>0:
    if df[col].dtype in [object , 'str']:
      df[col] = df[col].fillna(df[col].mode()[0])
    else:
      df[col] = df[col].fillna(df[col].mean())

#Drop Duplicated
df = df.drop_duplicates()

# Feature Engineering
df = df.drop(columns=['Month Number' , 'Month Name'])
df['GrossManuAmt'] = df['Units Sold'] * df['Manufacturing Price']

# Copy a dataset 
filtered_df = df.copy()

# Filters
col1 , col2 , col3 , col4 , col5 = st.columns(5)
with col1:
  country  = st.selectbox('Select Country' , ['All'] +  list(df['Country'].unique()))
  if country!= 'All':
    filtered_df = filtered_df[filtered_df['Country']==country]
with col2:
  segment  = st.selectbox('Select segment' , ['All'] +  list(df['Segment'].unique()))
  if segment!= 'All':
    filtered_df = filtered_df[filtered_df['Segment']==segment]
with col3:
  product = st.selectbox('Select Product', ['All'] + list(df['Product'].unique()))
  if product!='All':
    filtered_df = filtered_df[filtered_df['Product'] == product]
with col4:
  discount = st.selectbox('Select Discount' ,['All'] +  list(df['Discount Band'].unique()))
  if discount!='All':
    filtered_df = filtered_df[filtered_df['Discount Band'] == discount]
with col5:
  year = st.selectbox('Select Year' ,['All'] +  list(df['Year'].unique()))
  if year!='All':
    filtered_df = filtered_df[filtered_df['Year'] == year]

#KPIs Key Point Indicators
col1 , col2 , col3 , col4 , col5 = st.columns(5) 
with col1:
  st.metric('Total Sales : ' , round(filtered_df[' Sales'].sum(),2))
with col2:
  st.metric('Gross Manufacturing Amount' , round(filtered_df['GrossManuAmt'].sum(),2))
with col3:
  st.metric('Total Profit' , filtered_df['Profit'].sum().round(2), delta= filtered_df['Profit'].sum().round(2))
with col4:
  st.metric('Sold Quantity' , filtered_df['Units Sold'].sum().round(2))
with col5:
  st.metric('Total No. of Sales' , filtered_df.shape[0])

# Sample Dataset View
st.dataframe(filtered_df , height=250)
st.text('Dataset Shape : ' +  str(filtered_df.shape))