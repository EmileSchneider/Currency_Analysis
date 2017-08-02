import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from random import randint 

df = pd.read_csv("eur_chf.csv")
"""
hist = df['Open'].hist() #erzeugt das Histogram
hist.plot() #zeichnet das Histogram
plt.show() #gibt das gezeichnete Histogram aus
"""
# --- === open2open === ---
#create the open2open % change dataframe
open2open_percent_change = df['Open'].pct_change()

#histogramm
#bins for the histogramm
open2open_bins = [-0.03, -0.027, -0.024, -0.021, -0.017, -0.015, -0.012, -0.009, -0.006, -0.003, 0, 0.003, 0.006, 0.009, 0.012, 0.015, 0.018, 0.021, 0.024, 0.027, 0.03]
open2open_hist = open2open_percent_change.hist(xlabelsize = 0.003, bins = open2open_bins)
open2open_hist.plot()

#get descriptive statistics, like mean, median, std.dev etc
open2open_descriptive_statistics = open2open_percent_change.describe()

#average return:
open2open_average_return = open2open_percent_change.average()

#average positive return:
opn2open_percent_change_only_positive = open2open_percent_change[open2open_percent_change < 0] = None
open2open_average_positive_return = opn2open_percent_change_only_positive.mean()

#average negativ return
open2open_percent_change_only_negative = open2open_percent_change[open2open_percent_change > 0] = None
open2open_average_negative_return = open2open_percent_change_only_negative.mean()

#Count and Probabilites AND Cum.Probs.
count_open2open = open2open_percent_change.count()
count_open2open_positive = open2open_percent_change_only_positive.count()
count_open2open_negative = open2open_percent_change_only_negative.count()

count_open2open_negative_in_percent = () #wie ging prozentrechung nochmal? lieber im Video nachschauen. 
count_open2open_positive_in_percent = ()
zero_count_open2opne_positive_in_percent = () #gott auch das noch >()



# --- === low2high === --- 
#drop the unnecessary collumns:
low2high = df.drop('Open', axis = 1) #call by value OR call by reference?
low2high = low2high.drop('Price', axis = 1)
low2high = low2high.drop('Date', axis = 1)
low2high = low2high.drop("Change in%", axis = 1)
low2high_percent_change = low2high.pct_change(axis = 1) #are U sure it calculates the percentage change form the day_low to the day_high? bcs i am not sure
#need to swap the collumns, needs to be from LOW to HIGH,
#after swapping do the same as upstairs, it is probably a good idea to abstract this whole shit than to retype it here...

plt.show()