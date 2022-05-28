# Data Analysis for Automotive Industry

This is a Web - based Application build as a project for Microsoft Engage 2022 Mentorship Program. It can be acessed here: https://automotivedataanalysis.herokuapp.com/. 

Demo Video : https://youtu.be/RwXDOjSxBUU 

Two sample datasets are present in this repository which can be used to test the site. (car_sales.csv and cars_engage_2022.csv)

## Problem Statement

To Develop an application to demonstrate how the Automotive Industry could harness data to take informed decisions.

## Application Description 

The application helps the automotive industry to make sense of entered dataset. The user can enter a dataset relating to the automotive industry in the form of a csv or excel file. The webiste displays the dataset statistics, visualization and answers some specific queries. The website shows different market segments and the user can enter vehicle specifications and find out which other vehicles belong to the same segment and can be expected to compete with the entered vehicle. This feature is supported with visualization where the user can see the relation between different vehicle features based on segments. 

## Application Structure and Functionality

Once the data file has been uploaded, there are four sections which the user can explore. 

The four sections are as follows : 

* ### General Overview 
  This section displays the overall statistics of the enteres dataset, like number of rows, columns and so on. Apart from this, it also has a dropdown list from which  the user can select any one of the column names of the dataset. The details of the selected column along with a graph showcasing the data distribution will be displayed.   It will display frequencies of different values for object type columns and statistics for numeric columns .
  
  This section is to help the user understand the kind of dataset it is and get the basic layout of all the variables which is very important while making any decision with the help of data analysis. 
  
* ### Visualization
  This section allows user to see plots between different variables. The user can choose the variables from dropdown menus along with a column on which color gradient for the plots will be based. By default, there is no color gradient. This visualization can help answer some very basic queries, like the relationship between sales and price. Looking at the plots can easily answer the question "Which Price range has most sales ? " or a plot between Engine-Type and Horsepower can answer the question of "Which engine-type is related to the highest Horsepower ? " One can choose to have a color gradient of price which would also show the variation of price in the same plot. Similarly, there are a lot of simple queries that can be answered through the visualization between different variables. 
  
* ### Filter
  This section allows user to filter through the dataset. There are sliders which can be adjusted to specific range of values and data relating to that will be displayed. Some queries can be answered simply by doing a filter. Queries like "Vehicles in a certain price range" or "Vehicles with engine-capacity 1.8" or "Five vehicles with highest horsepower" can be answered through this feature. Clicking on the column name will arrange the data in ascending or descending order based on that column. 
  
* ### Specific Queries 
  This section is again divided into three parts as follows : 
  
  * #### Popular Vehicle Specification by Sales
    This displays the three most sold vehicles and their details.
  * #### Most Expensive Vehicles
    This displays the three most costly vehicles and their details.
  * #### Competing Segments
    This section divides the vehicles into different segments based on their details. The vehicles are clustered together into five different categories using K-Means clustering. Most vehicle markets can be optimally divided into five segments. The user can choose to search for the segment that an existing vehicle in the database belongs to or enter new specifications and check the segments. Visualization is also available which allows user to plot relation between different variables with the color gradient representing the different segments. This makes it easy to see which car belongs to which segment and what the properties of that segment are. Fo example, a car manufactured by Tata may belong to segment 1(as seen from the search function) which is the second most expensive segment (as seen from the plot). 
    
These features can allow the automotive companies to be aware of the various market segments and the cars they will be competing, the most popular specifications and other such queries which would help in making informed choices. 

## Techstack 
* Python - version 3.9.5 or greater (The deployed version is 3.10.4)
* Streamlit - version 1.9.0

Other library packages and dependencies are mentioned in the requirements.txt file

## Cloud Service 
* Heroku 

## Instructions to run on local machine 

* Ensure all the requirements mentioned in the requirements.txt file is met and the files are downloaded on your local machine.
* Go to the directory where the files are stored and use the following command in the command prompt : streamlit run app.py

## Note : 
* The sample datasets have been taken from Kaggle
* In case the website is not available, follow the instructions to run on local machine.
* The website expects input similar to the sample files provided, that is, it should have information about cars and have details like Price and Sales. Otherwise, some features won't work and an error message will be displayed. The program looks for columns named "Price" and "Sales" for some analysis. There are some alternatives that will work like "Price_in_thousands" or "Sales_in_thousands" but the column containing car prices cannot be named something like "Showroom". It will show an error similar to "Price not found". Change the name of the column and upload again in that case. 
* While entering data for new car specifications in the competing segment section, ensure that the data entered is of the same format as the examples mentioned there.
