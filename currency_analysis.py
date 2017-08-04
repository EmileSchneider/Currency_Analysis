import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from random import randint 

import tkinter 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

df = pd.read_csv("eur_chf.csv")
# --- === open2open === ---
#create the open2open % change dataframe
open2open_percent_change = df['Open'].pct_change()

#histogramm
#bins for the histogramm
open2open_bins = [-0.03, -0.027, -0.024, -0.021, -0.017, -0.015, -0.012, -0.009, -0.006, -0.003, 0, 0.003, 0.006, 0.009, 0.012, 0.015, 0.018, 0.021, 0.024, 0.027, 0.03]
open2open_hist = open2open_percent_change.hist(xlabelsize = 0.003, bins = open2open_bins)
#open2open_hist.plot()

#get descriptive statistics, like mean, median, std.dev etc
open2open_descriptive_statistics = open2open_percent_change.describe()

#average return:
open2open_average_return = open2open_percent_change.mean()

#average positive return:
open2open_percent_change_only_positive = []
for i in open2open_percent_change:
    if i > 0:
        open2open_percent_change_only_positive.append(i)
#change list to dataframe
open2open_percent_change_only_positive = pd.DataFrame(np.array(open2open_percent_change_only_positive))


open2open_average_positive_return = open2open_percent_change_only_positive.mean()

#average negativ return
open2open_percent_change_only_negative = []
for i in open2open_percent_change:
    if i < 0:
        open2open_percent_change_only_negative.append(i)
        
open2open_percent_change_only_negative = pd.DataFrame(np.array(open2open_percent_change_only_negative))        
open2open_average_negative_return = open2open_percent_change_only_negative.mean()

#Count and Probabilites AND Cum.Probs.
count_open2open = open2open_percent_change.count()
count_open2open_positive = open2open_percent_change_only_positive.count()
count_open2open_negative = open2open_percent_change_only_negative.count()

#count 0 values
helper_list = []

for i in open2open_percent_change:
    if i == 0:
        helper_list.append(i)

count_open2open_zero = len(helper_list)

#prozentualer Anteil der Neg and Pos Returns am Gesamtbild
count_open2open_negative_in_percent = (count_open2open_negative / count_open2open) 
count_open2open_positive_in_percent = (count_open2open_positive / count_open2open)
zero_count_open2open_positive_in_percent = (count_open2open_zero / count_open2open) 


# --- === low2high === --- 
low_list = df['Low'].values.tolist()
high_list = df['High'].values.tolist()

low2high_percent_change = []
for index in range(0,len(low_list)):
    a = low_list[index]
    b = high_list[index]

    low2high_percent_change.append((b - a)/ a)


low2high_bins = [0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022, 0.024, 0.026, 0.028, 0.03, 0.032, 0.034, 0.036, 0.038, 0.04]

#histogramm
#bins for the histogramm
low2high_bins = [0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022, 0.024, 0.026, 0.028, 0.03, 0.032, 0.034, 0.036, 0.038, 0.04]

#change list to dataframe
low2high_percent_change = pd.DataFrame(np.array(low2high_percent_change))


low2high_hist = low2high_percent_change.hist(xlabelsize = 0.002, bins = low2high_bins) #why is this an numpy array? WTF man...

#low2high_hist.plot() # # wwtf i do not need this? why... -.- 

#get descriptive statistics, like mean, median, std.dev etc
low2high_descriptive_statistics = low2high_percent_change.describe()

#average return:
low2high_average_return = low2high_percent_change.mean()


# --- === GUI === ---

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack()

histogram_frame = tkinter.Frame(root)
histogram_frame.pack(side = tkinter.TOP)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

canvas = FigureCanvasTkAgg(f, histogram_frame)
canvas.show()
canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

g = Figure(figsize=(5,5), dpi=100)
b = g.add_subplot(111)
b.plot([13,23,33,43,53,63,73,83],[25,26,21,23,28,29,23,25]) #das muss durch die Histgoramme open2open_hist und low2high_hist ersetzt werden, geht aber nicht

canvas = FigureCanvasTkAgg(g, histogram_frame)
canvas.show()
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, histogram_frame)
toolbar.update()
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

bottomframe = tkinter.Frame(root)
bottomframe.pack(side = tkinter.BOTTOM)
# die TExt Lables die unter den Histogrammen sein sollen sollten eig durch die Variablen die OBEN berechnet wurden beschriftet werden, werden sie aber nicht
label1 = tkinter.Label(bottomframe, textvariable = str(open2open_average_return) , relief = tkinter.RAISED)
label1.pack( side = tkinter.TOP)



root.mainloop()
#plt.show()