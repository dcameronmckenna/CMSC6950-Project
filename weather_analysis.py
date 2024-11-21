from datetime import date
import pandas as pd
import numpy as np
weather_data = pd.read_csv('en_climate_daily_NL_8403505_2020_P1D.csv', usecols=range(4,31), index_col='Date/Time')


def monthly_mean_temp(dataframe, month):
    weather_data = dataframe
    num_cols_mean_temp = ['Mean Temp (°C)']
    weather_data[num_cols_mean_temp] = weather_data[num_cols_mean_temp].astype(float) 
    mean_temp = weather_data[num_cols_mean_temp]
    first_day = (date(2020, month, 1) - date(2020, 1, 1)).days
    last_day = (date(2020, month+1, 1) - date(2020, 1, 1)).days 
    
    print("first day is", first_day)
    print("last day is", last_day)
    actualmean = mean_temp[first_day:last_day].mean()
    print(actualmean)
    return actualmean

def yearly_mean_temp(dataframe):
    monthly_mean = []
    for i in range(11):
        print(i)
        monthly_mean.append(monthly_mean_temp(dataframe, i+1))
    
    return monthly_mean

def monthly_rainy_days(dataframe, month):
    weather_data = dataframe
    num_cols_rain = ['Total Rain (mm)']
    weather_data[num_cols_rain] = weather_data[num_cols_rain].astype(float)
    total_rain = weather_data[num_cols_rain]


    first_day = (date(2020, month, 1) - date(2020, 1, 1)).days
    last_day = (date(2020, month+1, 1) - date(2020, 1, 1)).days 

    rainy_days = np.count_nonzero(total_rain[first_day:last_day])
    rain_amount = total_rain[first_day:last_day].sum()
    return rainy_days, rain_amount

def monthly_snowy_days(dataframe, month):
    weather_data = dataframe
    num_cols_snow = ['Total Snow (cm)']
    weather_data[num_cols_snow] = weather_data[num_cols_snow].astype(float)
    total_snow = weather_data[num_cols_snow]

    first_day = (date(2020, month, 1) - date(2020, 1, 1)).days
    last_day = (date(2020, month+1, 1) - date(2020, 1, 1)).days 

    snowy_days = np.count_nonzero(total_snow[first_day:last_day])
    snow_amount = total_snow[first_day:last_day].sum()
    return snowy_days, snow_amount

def above_mean_quantile(dataframe, column, mean):
    col_float = weather_data[column].astype(float)
    monthly_data = col_float[0:31]
    mask_higher = monthly_data > mean
    above_mean = monthly_data[mask_higher]

    quant = monthly_data.quantile([0.75])
    top = monthly_data > quant.loc[0.75]
    above_quantile = monthly_data[top]

    return above_mean, above_quantile


def below_mean_quantile(dataframe, column, mean):
    col_float = weather_data[column].astype(float)
    monthly_data = col_float[0:31]
    mask_lower = monthly_data < mean
    below_mean = monthly_data[mask_lower]

    quant = monthly_data.quantile([0.25])
    bottom = monthly_data > quant.loc[0.25]
    below_quantile = monthly_data[bottom]

    return below_mean, below_quantile



m1, q1 = above_mean_quantile(weather_data, 'Max Temp (°C)', 0)
print(m1,q1)