import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from multiapp import MultiApp
import page0, page1, page2, page3, page4, Data_cleaning
import re

st.set_page_config(
	page_title = 'Data Analysis',
	layout = "wide"
	)

try :  
	st.header("Data Analysis for Automotive Industry")
	data = page0.input() 

	menu = ["Select", "General Overview", "Visualization", "Filter Data", "Specific Queries"]
	choice = st.selectbox("Menu", menu)

	if choice == "General Overview" : 
		page1.Report(data)
	if choice == "Visualization" : 
		data = Data_cleaning.outliers(data)
		page2.Visual(data)
	if choice == "Filter Data" : 
		data = Data_cleaning.outliers(data)
		data = Data_cleaning.clean(data)
		page3.custom_filter(data)
	if choice == "Specific Queries" : 
		data = Data_cleaning.outliers(data)
		data = Data_cleaning.clean(data)
		Sales_column = ['Sales', 'sales', 'Sales_in_thousands', 'sales_in_thousands', 'sales_in_thousand', 'Car_Sales', 'car_sales']
		sales_title = 'Sales_in_thousands'
		for i in Sales_column : 
			if i in data.columns : 
				sales_title = i

		Price_column = ['Price_in_thousands','price_in_thousands', 'price_in_thousand', 'Price', 'price', 'Showroom_Price', 'showroom_price', 'Showroom_price', 'Car_price', 'car_price', 'Sale_price', 'Cost_price']
		price_title = 'Price_in_thousands'
		for i in Price_column : 
			if i in data.columns : 
				price_title = i

		e1 = 0
		e2 = 0
		if not(sales_title in data.columns) : 
			st.error('Sales data not found ! Ensure that the column name is set as Sales, Sales_in_thousands or car_sales')
			e1 = 1

		if not(price_title in data.columns) : 
			st.error('Price data not found ! Ensure that the column name is set as Price, Price_in_thousands or car_price')
			e2 = 1

		if e1 == 1 & e2 == 1 : 
			q = st.selectbox("Queries", ["Competing Segments"])
		elif e1 == 1 : 
			q = st.selectbox("Queries", ("Most Expensive vehicles", "Competing Segments"))
		elif e2 == 1 : 
			q = st.selectbox("Queries", ("Popular Vehicle specification by Sales", "Competing Segments"))
		else : 
			q = st.selectbox("Queries", ("Popular Vehicle specification by Sales", "Most Expensive vehicles", "Competing Segments"))

		if q == "Popular Vehicle specification by Sales" : 
			page4.popular(data, sales_title)
		if q == "Most Expensive vehicles" : 
			page4.popular(data, price_title)
		if q == "Competing Segments" :
			try : 
				if e2!= 1 : 
					data[price_title] = [re.sub('[^0-9]+', '', _) for _ in data[price_title]]
					data[price_title] = pd.to_numeric(data[price_title])
			except : 
				pass 
			page4.market_segment(data)

except : 
	st.error('Error Encountered ! Please check the correct data file is uploaded !')
