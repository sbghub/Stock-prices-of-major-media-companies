# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:48:09 2015

@author: Somak
"""

import matplotlib.pyplot as plot
import Quandl
import pandas as pda

'''
Shows the stock prices of ABC, CBS, FOX and VIA (Viacom) over 10 years
Little practice with matplotlib and Quandl
Also curious to see how these companies' performances correlate
Ought to fix the x and y portions of the graph
'''


# list of company tickers to check prices for
comp = ["ABC", "CBS", "FOX", "VIA"]

# pulls data from Quandl API for Nov 20th 2006 to Nov 20th 2016
for name in comp:
    mydata = Quandl.get(
        "YAHOO/" + name,
        trim_start="2006-11-20",
        trim_end="2016-11-20"
    )
# makes specific Dataframes for Close prices and Ex-Dividend values
s = pda.DataFrame(mydata)
x = pda.DataFrame(s['Close'])
d = pda.DataFrame(s['Ex-Dividend'])

# appends Close prices to list for matplotlib to handle
y, z, i = [], [], 1
while i < len(x):
    y.append(x.values[i:i+1])
    i += 1
# combines z and y values for Adj-close
z = z + y

# basic plot of data
plot.plot(x, label=name)


plot.legend(loc=0, frameon=False, title="Stock Prices / Days")
plot.plot(z, label="TV")
