import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns

time_series = pd.read_csv('https://raw.githubusercontent.com/rjrahul24/ai-with-python-series/main/05.%20Build%20Concrete%20Time%20Series%20Forecasts/Data/DailyDelhiClimateTrain.csv', parse_dates=['date'], index_col='date')
time_series.head()

time_series.plot(subplots=True)

time_series.mean()

time_series.max()

time_series.min()

time_series.describe()

timeseries_mm = time_series['wind_speed']
timeseries_mm.plot(style='g--')
plt.show()

timeseries_mm = time_series['wind_speed'].resample("A").mean()
timeseries_mm.plot(style='g--')
plt.show()

time_series['wind_speed'].rolling(window=14, center=False).mean().plot(style='-g')
plt.show()

from pandas import Series,DataFrame
import statsmodels
from statsmodels.tsa.stattools import adfuller

time_series_train = pd.read_csv('https://raw.githubusercontent.com/rjrahul24/ai-with-python-series/main/05.%20Build%20Concrete%20Time%20Series%20Forecasts/Data/DailyDelhiClimateTrain.csv', parse_dates=True)
time_series_train["date"] = pd.to_datetime(time_series_train["date"])
time_series_train.date.freq ="D"
time_series_train.set_index("date", inplace=True)
time_series_train.columns

from statsmodels.tsa.seasonal import seasonal_decompose
sd_1 = seasonal_decompose(time_series_train["meantemp"])
sd_2 = seasonal_decompose(time_series_train["humidity"])
sd_3 = seasonal_decompose(time_series_train["wind_speed"])
sd_4 = seasonal_decompose(time_series_train["meanpressure"])
sd_1.plot()
sd_2.plot()
sd_3.plot()
sd_4.plot()

adfuller(time_series_train["meantemp"])
adfuller(time_series_train["humidity"])
adfuller(time_series_train["wind_speed"])
adfuller(time_series_train["meanpressure"])

# Consolidate the ad-fuller tests to test from static data
temp_var = time_series_train.columns
print('significance level : 0.05')
for var in temp_var:
    ad_full = adfuller(time_series_train[var])
    print(f'For {var}')
    print(f'Test static {ad_full[1]}',end='\n \n')





