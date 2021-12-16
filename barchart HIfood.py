# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:45:04 2021

@author: jenru
"""

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# lambda function that converts a string into datetime
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')

# Path of the file to read
HIfood_filepath = "C:/Users/jenru/Maui Data Files/HIPoundsFood.csv"

# Read the file into a variable HI_food
HI_food = pd.read_csv(HIfood_filepath, index_col="Date")

#print the data
HI_food

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Pounds of Food Produced in Hawaii, by Year")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=HI_food.index, y=HI_food['Pounds of Food'])

# Add label for vertical axis
plt.ylabel("Pounds of Food")
