import weather_analysis
import pandas as pd
import pytest


weather_data = pd.read_csv('en_climate_daily_NL_8403505_2020_P1D.csv',
                            usecols=range(4,31), index_col='Date/Time')

@pytest.mark.parametrize("dataframe, month, expected",
                         [(weather_data, 1, -4.706452),
                          (weather_data, 2, -4.246429),
                          (weather_data, 3, -3.083333),
                          ])
def test_monthly_mean_temp(dataframe, month, expected):
    observed = float(weather_analysis.monthly_mean_temp(dataframe, month))
    assert abs(observed-expected) < 1e-5

@pytest.mark.parametrize("dataframe, expected",
                         [(weather_data, [-4.706452, -4.246429, -3.083333, 1.253333, 6.645161, 13.826667,
                                          14.01, 17.370968, 14.748276, 8.664516, 3.434483, 2.022581]),
                          ])
def test_yearly_mean_temp(dataframe, expected):
    observed = weather_analysis.yearly_mean_temp(dataframe)
    print(observed)
    for i in range(len(observed)):
        observed[i] = float(observed[i])
        assert abs(observed[i]-expected[i]) < 1e-5
    
@pytest.mark.parametrize("dataframe, month, expected1, expected2",
                         [(weather_data, 1, 8, 26.8),
                          (weather_data, 2, 5, 38.3),
                          (weather_data, 3, 14, 86.8),
                          ])
def test_monthly_rainy_days(dataframe, month, expected1, expected2):
    observed1, observed2 = weather_analysis.monthly_rainy_days(dataframe, month)
    observed1 = float(observed1)
    observed2 = float(observed2)
    assert observed1 == expected1
    assert abs(observed2-expected2) < 1e-5
    
    
@pytest.mark.parametrize("dataframe, month, expected1, expected2",
                         [(weather_data, 1, 22, 172.8),
                          (weather_data, 2, 15, 85.1),
                          (weather_data, 3, 15, 70.6),
                          ])
def test_monthly_snowy_days(dataframe, month, expected1, expected2):
    observed1, observed2 = weather_analysis.monthly_snowy_days(dataframe, month)
    observed1 = float(observed1)
    observed2 = float(observed2)
    assert observed1 == expected1
    assert abs(observed2-expected2) < 1e-5
    

#pytest.param("two thousand twenty two", 1, 1, 2, marks=pytest.mark.xfail(reason='string input is invalid'))