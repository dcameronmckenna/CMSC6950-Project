from datetime import date
import pandas as pd
weather_data = pd.read_csv('en_climate_daily_NL_8403505_2020_P1D.csv', usecols=range(4,31), index_col='Date/Time')


def monthly_mean_temp(dataframe, month):
    weather_data = dataframe
    num_cols_mean_temp = ['Mean Temp (°C)']
    weather_data[num_cols_mean_temp] = weather_data[num_cols_mean_temp].astype(float) 
    mean_temp = weather_data[num_cols_mean_temp]
    first_day = (date(2020, month, 1) - date(2020, 1, 1)).days
    last_day = (date(2020, month+1, 1) - date(2020, 1, 1)).days - 1
    
    print("first day is", first_day)
    print("last day is", last_day)
    actualmean = mean_temp[first_day:last_day].mean()
    print(actualmean)
    return actualmean

print(monthly_mean_temp(weather_data, 1))

