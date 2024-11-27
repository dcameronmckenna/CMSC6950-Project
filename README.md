# CMSC6950 Project: Analyzing Weather Data from St. John's, NL in January 2020
(Weather Data recorded at the St. John's International Airport)

## Overview

The aim of this project was to analyze weather data from the month of January 2020, during which the significant snowfall named "Snowmaggedon" took place. We wanted to discover whether there were any other significant weather events that took place during the month, and to look at weather trends for the month overall. 

The data set used recorded several different aspects of the weather on a daily basis for the year 2020 (however other years which fit the same format could be used). The columns of the data set pertaining to the measured data are `Max Temp`, `Min Temp`, `Mean Temp`, `Heat Deg Days`, `Cool Deg Days`, `Total Rain (mm)`, `Total Snow (cm)`, `Total Precip (mm)`, `Snow on Grnd (cm)`, `Dir of Max Gust (10s deg)`, and `Spd of Max Gust (km/h)`. All temperature values are in celcius. There are separate flag columns for each column of data measured to indicate any special conditions for the data; the legend for the flag columns can be found on the website where the dataset is available. 

## Graphs and Figures

All graphs and figures can be found in the file `project_graphs.ipynb` which is inside the folder `project_graphs`. For each graph/figure, we import the data from a CSV file, and plot the first 31 days of each different weather column that we analyzed. Finally, all graphs/figures are saved as PDFs. If you would like to plot the weather data for a different month, you will have to update the slicing on the data set to reflect the days of that month. 

The last line in the file `project_graphs.ipynb` provides a description of the data during the month of January 2020, which can also be useful for finding the mean, standard deviation, minimum, maximum, and quartiles of the data set. 

## Weather Analysis

Several functions to analyze different aspects of the weather are available for use in the file `weather_analysis.py`. 
- `monthly_mean_temp` takes a dataframe and a month and finds the mean temperature of the daily mean temperature for that month.
- `yearly_mean_temp` takes a dataframe and collects all of the monthly mean temperatures for the year in a list.
- `monthly_rainy_days` takes a dataframe and a month and returns the number of rainy days in a given month and the total amount of rain that fell during the month.
- `monthly_snowy_days` takes a dataframe and a month and returns the number of snowy days in a given month and the total amount of snow that fell during the month.
- `above_mean` takes a dataframe, a column of that dataframe, a given mean, and a month and returns all of the days in that column where the value of the day is higher than the given mean in a series. 
- `below_mean` takes a dataframe, a column of that dataframe, a given mean, and a month and returns all of the days in that column where the value of the day is lower than the given mean in a series.
- `high_speed_winds` takes a dataframe, a given speed, and a month and returns all of the days in the month where the maximum wind gust speed was above the given value for wind speed.

Tests for all of these functions are provided in the file `test_weather_analysis`. 

## Links

- Weather data used in the project, and other data which could be evaluated is found [here](https://climate.weather.gc.ca/climate_data/daily_data_e.html?timeframe=2&hlyRange=2012-03-20%7C2024-09-30&dlyRange=2012-03-20%7C2024-09-30&mlyRange=%7C&StationID=50089&Prov=NL&urlExtension=_e.html&searchType=stnName&optLimit=yearRange&StartYear=1840&EndYear=2024&selRowPerPage=25&Line=7&searchMethod=contains&txtStationName=st.+john%27s&Day=30&Year=2020&Month=1#). 
- Historical averages for St. John's weather can be found [here](https://www.theweathernetwork.com/ca/historical/newfoundland-and-labrador/st-johns). 
- Criteria for weather alerts in Canada can be found [here](https://www.canada.ca/en/environment-climate-change/services/types-weather-forecasts-use/public/criteria-alerts.html).
