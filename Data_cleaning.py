import numpy as np 
import pandas as pd
import re
import streamlit as st

def outliers(df) : 
	for x in df.columns : 
		missing = df[x].isnull().sum()
		percent = round(missing / len(df[x]) * 100)
		if percent > 5 : 
			df = df.drop(columns = x)

	for i in df.columns : 
		df = df[~df[i].isnull()]

	df = df.reset_index(drop = True)
	return df

def clean(df) : 

	org_df = df.copy()

	n_cols = df.select_dtypes(include = object)

	for column in n_cols.columns : 
		try : 
			l = re.findall(r"[^\W\d_]+|\d+", df.loc[0, column])
			str = l[len(l) - 1]
			if str.isdigit() :
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
				df[column] = [re.sub('[^0-9]+', '', _) for _ in df[column]]
				df[column] = pd.to_numeric(df[column])
		except : 
			df[column] = org_df[column]

	for i in df.columns : 
		df = df[~df[i].isnull()]

	return df

