import pandas as pd
import numpy as np
import streamlit as st

def input():
	st.subheader("Dataset")
	data_file = st.file_uploader("Upload Excel or CSV file", type = ["csv", "xlsx", "xls"])
	if data_file is not None:
		try : 
			df = pd.read_excel(data_file)
			st.dataframe(df)
			return df
		except : 
			try : 
				df = pd.read_csv(data_file)
				st.dataframe(df)
				return df
			except : 
				st.error("Incompatible file type ! Upload a csv or excel file")

		