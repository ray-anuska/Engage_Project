# Data Analysis for Automotive Industry

This is a Web - based Application build as a project for Microsoft Engage 2022 Mentorship Program. It can be acessed here: https://automotivedataanalysis.herokuapp.com/. 
Two sample datasets are present in this repository which can be used to test the site. (car_sales.csv and cars_engage_2022.csv)

## Problem Statement

To Develop an application to demonstrate how the Automotive Industry could harness data to take informed decisions.

## Application Description 

The application helps the automotive industry to make sense of entered dataset. The user can enter a dataset relating to the automotive industry in the form of a csv or excel file. The webiste displays the dataset statistics, visualization and answers some specific queries. The website shows different market segments and the user can enter vehicle specifications and find out which other vehicles belong to the same segment and are which can be expected to compete with the entered vehicle. This feature is supported with visualization where the user can see the relation between different vehicle features based on segments. 

## Application Structure and Functionality

Once the data file has been uploaded, there are four sections which the user can explore. 

The four sections are as follows : 

* ### General Overview 
  This section displays the overall statistics of the enteres dataset, like number of rows, columns and so on. Apart from this, it also has a dropdown list from which  the user can select any one of the column names of the dataset. The details of the selected column along with a graph showcasing the data distribution will be displayed.   It will display frequencies of different values for object type columns and statistics for numeric columns .
  
  This section is to help the user understand the kind of dataset it is and get the basic layout of all the variables which is very important while making any decision with the help of data analysis. 
  
* ### Visualization
  This section allows user to see plots between different variables. The user can choose the variables from dropdown menus along with a column on which color gradient for the plots will be based. By default, there is no color gradient. This visualization can help answer some very basic queries, like the relationship between sales and price. Looking at the plots can easily answer the question "Which Price range has most sales ? " or a plot between Engine-Type and Horsepower can answer the question of "Which engine-type is related to the highest Horsepower ? " One can choose to have a color gradient of price which would also show the variation of price in the same plot. Similarly, there are a lot of simple queries that can be answered through the visualization between different variables. 
