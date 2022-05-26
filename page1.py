import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

def details(x, title) : 
	distinct = x.unique()
	st.metric(label = "Distinct Values : " , value = len(distinct))
	numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
	if(x.dtype in numerics) : 
		stat = x.describe()
		st.dataframe(stat)
	else :
		count = x.value_counts()
		count = count.to_frame()
		count.rename(columns = {title : "Frequency"}, inplace = True)
		st.dataframe(count)
		
def Report(df) : 

	st.header("Dataset Statistics")
	ncols = len(df.columns)
	nrows = len(df)
	total_missing = df.isnull().sum().sum()
	percentage_missing = round(total_missing/(ncols * nrows) * 100)
	duplicate = df[df.duplicated()]
	n_dup = len(duplicate)
	percentage_duplicate = round(n_dup / (ncols * nrows) * 100)
	df = df[~df.duplicated()] #dropping duplicate rows

	col1, col2, col3 = st.columns(3)
	with col1 : 
		st.metric(label = "Numeber of variables", value = ncols)
		st.metric(label = "Number of rows of data" , value = nrows)

	with col2 : 
		st.metric(label = "Total number of Missing values " , value = total_missing)
		st.metric(label = "Missing" , value = str(percentage_missing) + "%") 
	
	with col3 : 
		st.metric(label = "Number of Duplicate rows " , value = n_dup)
		st.metric(label = "Duplicates" , value = str(percentage_duplicate)+ " % ")


	options = df.columns.tolist()
	var = st.selectbox("Variables", options)
	st.header(var)
	col1, col2 = st.columns(2)

	with col1 : 
		details(df[var], var)


	with col2 :  
		fig, ax = plt.subplots()
		fig = px.bar(df, x = var)
		st.plotly_chart(fig)


	
