import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.express as px
import streamlit as st
import sys 

def dashboard(sorted_df, rank) :
	cols = len(sorted_df.columns)

	with st.container() : 
			h = str(rank) + ". " + str(sorted_df.iloc[rank - 1, 0])
			st.header(h)

	rank = rank - 1

	col1, col2, col3,col4 = st.columns(4)

	with col1 : 
		for i in range(0, cols, 4) : 
			#st.write("	", sorted_df.columns[i], ' : ', sorted_df.iloc[0, i])
			if sorted_df.iloc[rank, i] == sorted_df.iloc[rank, i] : 
				st.metric(label = sorted_df.columns[i], value = sorted_df.iloc[rank, i])
	with col2 : 
		for i in range(1, cols, 4) : 
			if sorted_df.iloc[rank, i] == sorted_df.iloc[rank, i] : 	
				st.metric(label = sorted_df.columns[i], value = sorted_df.iloc[rank, i])	
	with col3 : 
		for i in range(2, cols, 4) : 
			if sorted_df.iloc[rank, i] == sorted_df.iloc[rank, i] : 
				st.metric(label = sorted_df.columns[i], value = sorted_df.iloc[rank, i])	
	with col4 : 
		for i in range(3, cols, 4) : 
			if sorted_df.iloc[rank, i] == sorted_df.iloc[rank, i] : 	
				st.metric(label = sorted_df.columns[i], value = sorted_df.iloc[rank, i])


def popular(df, name) : 
	sorted_df = df.sort_values(by = name, ascending = False)
	sorted_df = sorted_df.head(3)

	dashboard(sorted_df, 1)
	dashboard(sorted_df, 2)
	dashboard(sorted_df, 3)

def market_segment(df) : 
	try : 

		num_cols = [ i for i in df.columns if df[i].dtype != 'object']

		for i in num_cols : 
			df = df[~df[i].isnull()]
		km = KMeans(n_clusters=5, n_init=20, max_iter=400, random_state=0)
		segment = km.fit_predict(df[num_cols])
		df['segment'] = segment
		df.segment = (df.segment + 1).astype('object')

		st.dataframe(df)

		col1, col2 = st.columns(2)

		with col1 : 

			st.write('Search for comepting vehicles for exisitng vehicle in database or Enter new specificatins below : ')
			c = st.selectbox('Select', ("Existing vehicle", "New Specifications"))
			if c == "Existing vehicle" : 
				menu = df.select_dtypes(include = object).columns
				menu = menu.insert(0, "None")
				s = st.selectbox("Search by ", menu)
				if s != "None" : 
					query = st.selectbox("Select", df[s].unique())
					s_segment = df[df[s] == query].segment
					s_segment = s_segment.unique()
					st.write('Details of vehicles with selected feature along with the segment it belongs to : ')
					st.dataframe(df[df[s] == query])
					result = df[pd.DataFrame(df.segment.tolist()).isin(s_segment).any(1).values]
					st.write('Other Competing Vehicles : ')
					st.dataframe(result)

			if c == "New Specifications" : 

				st.write("Enter new details not in database : ")
				newd = {}
				for i in num_cols : 
					input_ = st.text_input("Enter " + str(i) + " (for eg. " + str(df[i][0]) + " )")
					if input_ != "": 
						newd[i] = float(input_)
				new_df = pd.DataFrame(newd, columns = num_cols, index = [0])
				if new_df.isnull().values.any() == False: 
					st.dataframe(new_df)	
					frames = [df[num_cols], new_df]	
					new_df = pd.concat(frames)
					new_segment = km.fit_predict(new_df)
					st.write("Vehicle with entered specifications is part of segment no. " + str(new_segment[len(new_df) - 1]))
					st.write("Other vehicles in this segment : ")
					st.dataframe(df[df["segment"] == new_segment[len(new_df) - 1]])


		with col2 : 


			plot_type = st.selectbox("Select typr of plot", ("Scatter", "Bar"))
			x = st.selectbox("Variable 1 (x - axis)", df.columns) 
			y = st.selectbox("Variable 2 (y - axis)", df.columns)

			fig, ax = plt.subplots()
			if(plot_type == "Scatter") : 
				fig = px.scatter(df, x = x, y = y, color = "segment")
			if(plot_type == "Bar") : 
				fig = px.bar(df, x = x, y = y, color = "segment")
			
			st.plotly_chart(fig, use_container_width = True)

	except : 
		st.error("Not enough numeric values. Check entered data ! ")


