import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# lambda function that converts a string into datetime
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')

# reads the csv into 
df = pd.read_csv(r"C:/Users/jenru/Maui Data Files/HIPoundsFood.csv", parse_dates=['Date'], date_parser=dateparse)

# sets the date column as the index
#df = df.set_index('Date')



period = pd.Series(df['Date'])
ts = df['Pounds of Food']

# defines the function for exponential smoothing
def exp_smooth(y_true, alpha):
    y_pred = [y_true[0]]
    for n in range(1, len(y_true)-1):
        y_pred.append(alpha * y_true[n] + (1 - alpha) * y_pred[n - 1])
    y_pred = [np.NaN] + y_pred
    return y_pred

# plots the exponential smoothing forecast for alpha = 0.05, 0.1
plt.plot(period, ts,label = "Signal - Obs Values ");
plt.plot(period, exp_smooth(ts, 0.05),label = "Exp Smoothing (α = 0.05)");
plt.plot(period, exp_smooth(ts, 0.2),label = "Exp Smoothing (α = 0.1)");
plt.xlabel('Period', fontsize = 12);
plt.xticks(rotation='vertical')
plt.margins(0.12)
plt.subplots_adjust(bottom=0.05)
plt.ylabel('Pounds of Food Grown in Hawaii', fontsize = 12);
plt.legend(loc='upper left');
