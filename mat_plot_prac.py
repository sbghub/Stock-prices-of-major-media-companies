# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:48:09 2015

@author: Somak
"""
'''
Shows the stock prices of ABC, CBS, FOX and VIA (Viacom) over 10 years
Little practice with matplotlib and Quandl
Also curious to see how these companies' performances correlate
Ought to fix the x and y portions of the graph
'''


import matplotlib.pyplot as plot
import Quandl
import pandas as pda

comp = ["ABC", "CBS", "FOX", "VIA"]

for name in comp:
    mydata = Quandl.get(
        "YAHOO/" + name, 
        trim_start="2006-11-20", 
        trim_end="2016-11-20"
    )
s = pda.DataFrame(mydata)
x = pda.DataFrame(s['Close'])
d = pda.DataFrame(s['Ex-Dividend'])
y, z, i = [], [], 1

while i < len(x):
	y.append(x.values[i:i+1])
	i += 1

z = z + y
plot.plot(x, label = name)
    
    

plot.legend(loc = 0, frameon = False, title = "Stock Prices / Days")
plot.plot(z, label = "TV")
