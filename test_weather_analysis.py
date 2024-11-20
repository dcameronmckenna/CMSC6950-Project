import weather_analysis
import pandas as pd
import pytest


weather_data = pd.read_csv('en_climate_daily_NL_8403505_2020_P1D.csv', usecols=range(4,31), index_col='Date/Time')

@pytest.mark.parametrize("dataframe, month, expected",
                         [(weather_data, 1, -4.706452),
                          (weather_data, 2, -4.246429),
                          (weather_data, 3, -3.083333),
                          ])
def test_monthly_mean_temp(dataframe, month, expected):
    observed = float(weather_analysis.monthly_mean_temp(dataframe, month))
    assert abs(observed-expected) < 1e-5


def test_yearly_mean_temp(dataframe, expected):
    return NotImplementedError
    

def test_monthly_rainy_days(dataframe, month, expected):
    return NotImplementedError
    

def test_monthly_snowy_days(dataframe, month, expected):
    return NotImplementedError
    

#pytest.param("two thousand twenty two", 1, 1, 2, marks=pytest.mark.xfail(reason='string input is invalid'))