import numpy as np 
import pandas as pd 
import streamlit as st

def dslide_filter(x, title) : 
	max_limit = round(x.max())
	min_limit = round(x.min())
	output_range = st.slider(title, value = [min_limit, max_limit])
	mask = ((x >= output_range[0]) & (x <= output_range[1]))
	return mask 

def custom_filter(df) : 
	
	with st.sidebar : 
		st.write("Choose Filters")

		numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
		n_df = df.select_dtypes(include=numerics)
		
		mask = []
		for i in n_df.columns : 
			m = dslide_filter(n_df[i], i)
			mask.append(m)

		filtered_mask = mask[0]
		for i in mask : 
			filtered_mask = filtered_mask & i #adding the conditions from each slider
		
	st.dataframe(df.loc[filtered_mask])
