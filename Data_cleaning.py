import numpy as np 
import pandas as pd
import re
import streamlit as st

def outliers(df) : 
	for x in df.columns : 
		missing = df[x].isnull().sum()
		percent = round(missing / len(df[x]) * 100)
		if percent > 10 : #if missing values more than 10 percent then drop those columns
			df = df.drop(columns = x)

	for i in df.columns : 
		df = df[~df[i].isnull()] #dropping rows with empty or missing values

	df = df.reset_index(drop = True)#resetting the index after deleting some rows
	return df

def clean(df) : 

	org_df = df.copy()

	n_cols = df.select_dtypes(include = object)

	for column in n_cols.columns : 
		try : #checks if string follows pattern of "number unit" and if it does, removes the unit and makes column numeric
			#only checks first element of column assuming all will be same
			l = re.findall(r"[^\W\d_]+|\d+", df.loc[0, column])#separating the letters and digits
			str = l[len(l) - 1]
			if str.isdigit() :#if the last element is a digit then it means no unit to remove so onto the next column
				continue
			if len(l) == 1 : 
				continue
			l = l[0 : len(l) - 1] 
			f = 0
			for i in l : 
				if i.isdigit() : 
					continue
				else : 
					f = 1
					break 
			if f == 0 : 
				df[column] = [re.sub('[^0-9]+', '', _) for _ in df[column]]#keeping only the number and converting column to numeric type
				df[column] = pd.to_numeric(df[column])
		except : 
			df[column] = org_df[column]#restor original in case of any error

	for i in df.columns : 
		df = df[~df[i].isnull()]#remove any rows with missing values

	return df

