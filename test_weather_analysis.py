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

@pytest.mark.parametrize("dataframe, column, mean, month, expected_list",
                         [(weather_data, 'Max Temp (°C)', 0, 1, [1.6, 1.6, 0.5, 3.2,
                                                                 0.5, 4.4, 4.2, 1.7, 
                                                                 2.1, 0.6, 0.2, 4.6]),
                        (weather_data, 'Max Temp (°C)', -1, 2, [5.0, -0.4, -0.6, 6.2, 
                                                                8.1, 1.2, -0.8, -0.6, 
                                                                1.8, 5.2, 1.5, 1.5, 
                                                                4.0, 1.4, 0.5, 0.2]),
                          ])
def test_above_mean(dataframe, column, mean, month, expected_list):
    above_mean = weather_analysis.above_mean(dataframe, column, mean, month)
    for i in range(above_mean.shape[0]):
        assert above_mean.iloc[i].item() == expected_list[i]

@pytest.mark.parametrize("dataframe, column, mean, month, expected_list",
                         [(weather_data, 'Min Temp (°C)', -4, 1, [-5.3, -6.6, -6.9, -10.4,
                                                                  -13.4, -8.1, -11.3, -12.9, 
                                                                  -12.8, -12.9, -5.5, -15.4,
                                                                  -15.2, -6.5, -13.7, -16.3,
                                                                  -7.6, -11.3, -13.1, -9.4, 
                                                                  -6.0, -8.7]),
                        (weather_data, 'Min Temp (°C)', -5, 2, [-11.8, -8.3, -7.8, -7.9,
                                                                -7.2, -9.5, -6.6, -7.0,
                                                                -17.2, -15.9, -6.9, -11.7,
                                                                -11.9, -13.2, -13.3, -13.6,
                                                                -5.3, -7.8, -9.2]),
                          ])
def test_below_mean(dataframe, column, mean, month, expected_list):
    below_mean = weather_analysis.below_mean(dataframe, column, mean, month)
    for i in range(below_mean.shape[0]):
        assert below_mean.iloc[i].item() == expected_list[i]

@pytest.mark.parametrize("dataframe, speed, month, expected_list",
                         [(weather_data, 90, 1, [93.0, 93.0]),
                          (weather_data, 90, 2, [91.0, 118.0, 109.0])])
def test_high_speed_wind(dataframe, speed, month, expected_list):
    speed = weather_analysis.high_speed_winds(dataframe, speed, month)
    for i in range(speed.shape[0]):
        assert speed.iloc[i].item() == expected_list[i]