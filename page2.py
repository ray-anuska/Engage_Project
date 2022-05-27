import numpy as np 
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def Visual(df) : 

	col1, col2, col3, col4 = st.columns(4) 

	plot_type = "scatter"
	options = df.columns.tolist()
	options.insert(0, None)#insert None as an option which would be the default for color
	with col1 :
		plot_type = st.selectbox("Select type of plot", ("Scatter", "Bar"))

	with col2 : 
		x = st.selectbox("Variable 1 (x - axis)", df.columns)

	with col3 : 
		y = st.selectbox("Variable 2 (y - axis)", df.columns)

	with col4 : 
		color = st.selectbox("Choose variable to add color to plot : ",options) 

	fig, ax = plt.subplots()
	if(plot_type == "Scatter") : 
		fig = px.scatter(df, x = x, y = y, color = color)
		fig.update_traces(marker_size=10)
	if(plot_type == "Bar") : 
		fig = px.bar(df, x = x, y = y, color = color)


	
	st.plotly_chart(fig, use_container_width = True)

