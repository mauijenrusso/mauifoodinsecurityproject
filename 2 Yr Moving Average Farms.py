import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# lambda function that converts a string into datetime
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')

# reads the csv into 
df = pd.read_csv(r"C:/Users/jenru/Maui Data Files/HIfarms.csv", parse_dates=['Date'], date_parser=dateparse)

# sets the date column as the index
#df = df.set_index('Date')



period = pd.Series(df['Date'])
ts = df['Farms']

# creates MA series
mov_ave2 = ts.rolling(window=2, center=False).mean()
mov_ave14 = ts.rolling(window=4, center=False).mean()

#print(df['Farms'])
#print(mov_ave2)


# plots time series
plt.plot(period, ts,label = "Observed values");
plt.plot(period, mov_ave2,label = "2-MA");
plt.plot(period, mov_ave14,label = "4-MA");
plt.xlabel('Period', fontsize = 12);
plt.xticks(rotation='vertical')
plt.ylabel('Number of Farms and Ranch Operations', fontsize = 12);
plt.legend(loc='upper left');
plt.savefig("moving_average.png")

# impots the necessary modules
from sklearn.metrics import mean_squared_error

# finds the MAE and MSE for each forecasting technique
mean_squared_error(df['Farms'],mov_ave2)
mean_squared_error(df['Farms'],mov_ave14)
