# Habitomics

Given is the step by step process i have taken in order to implement and work around the problem statement


 **Problem statement** :- Using publicly available data on key factors that impact the prices of homes (US), build a data science model to understand how these factors have effected on home prices.

**Approach:** The following variables are chosen for the study:

1. Unemployment Rate
2. Working age
3. Per capita GDP
4. Median Household Income
5. house affordability
6. CPI
7. Interest Rates
8. Rental affordability
9. Working Population
10. Urban Population
11. Houses sold

As a proxy for home prices, the S&P **Case-Shiller Index** is used.

**Note:** Most of the data is downloaded from different websites linked in readme

Data for all the variables is downloaded, preprocessed, and combined to create a dataset using the **Extract Transform Load (ETL)** method. Data for different variables had different frequencies.



**Datasets used ***

Given here  are the links to the databases I have used for the creation of the entire process of house trends that affect prices

Here is the link for unemployment  rate  https://data.bls.gov/pdq/SurveyOutputServlet


Here is the link for interest rate in use https://fred.stlouisfed.org/series/FEDFUNDS

Here is the link for the house price proxies that I am using for this project 
https://fred.stlouisfed.org/series/CSUSHPINSA


Here is the link for Gdp  per capita of United States from 2000 to 2024 https://fred.stlouisfed.org/series/A939RC0Q052SBEA

Here is the link for mortgage rates in United States from 2000 to 2024 https://fred.stlouisfed.org/series/MORTGAGE30US

Here is the link for  consumer price index from 2000 
https://data.worldbank.org/indicator/FP.CPI.TOTL?locations=US&skipRedirection=true&view=map&year=2000

Here is the link for real household income https://fred.stlouisfed.org/series/MEHOINUSA672N

Here is the link for houses sold https://www.huduser.gov/portal/ushmc/hd_home_sales.html

Here is the link for houses created https://www.census.gov/construction/nrc/historical_data/index.html

Here is the link for affordability of homes https://www.huduser.gov/portal/ushmc/hd_hsg_aff.html

Here is the link for working age https://fred.stlouisfed.org/series/LFWA64TTUSM647S

Here is the link for urban population https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS?end=2023&locations=US&start=2000


There fore this ends the total amount of data that have been collected from publicly available data


Why eda  https://medium.com/dataseries/an-eda-checklist-800beeaee555

Here are the articles that I took reference to  understand how to read the data and collinearity 
 https://medium.com/@rokaandy/python-data-visualization-heatmaps-79fa7506c410

https://www.quanthub.com/how-to-read-a-correlation-heatmap/

Histogram :- https://www.labxchange.org/library/items/lb:LabXchange:10d3270e:html:1

What have I faced ? 

How do I make the visualisation interactive and dynamic there’s d3 and chart.js I could use but Figma too how is the thing related to product what should I keep in mind to make things simpler

How do I represent data in Figma , where do I input the dynamic data how should I represent


**Articles** used for understanding the factors 

------------------------------------------------------------------------------------
https://helenpainter.com/what-influences-home-value/
https://www.investopedia.com/articles/mortages-real-estate/11/factors-affecting-real-estate-market.asp
https://www.westernasset.com/us/en/research/blog/deciphering-factors-that-impact-the-us-housing-market-2024-03-13.cfm
https://point.com/blog/factors-that-affect-home-prices
https://www.economicshelp.org/blog/377/housing/factors-that-affect-the-housing-market/
https://fortune.com/2023/11/19/housing-prices-predictions-market-outlook-recession/
https://www.inc.com/inc-masters/how-the-us-presidential-election-may-impact-real-estate.html
  
