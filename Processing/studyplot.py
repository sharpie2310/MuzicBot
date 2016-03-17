# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:43:07 2016

@author: kshtz
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)


## the data
N = 5
('Marche', 28), ('Bourree', 26), ('Farandole', 22), ('---', 21), ('Polka', 15), ('Branle double', 14)
Input = [8.4, 7.8, 6.8, 6.6, 5.2]
Generated = [7.9, 2.8, 6.2, 5.93, 5.3]
#Input = [60.4, 10.2, 9.16, 8.9, 6.2]
#Generated = [57.3, 5.6, 2.24, 4.5, 4.44]
#Input = [12.8,11.95,11.95,11.95,10.4]
#Generated = [4.1,10.7,6.9,4.5,5.6]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.35                      # the width of the bars

## the bars
rects1 = ax.bar(ind, Input, width,
                color='green')

rects2 = ax.bar(ind+width, Generated, width,
                    color='red')

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,15)
ax.set_ylabel('%Tunes')
xTickMarks = ['sl\"angpolska','polska','vals','schottis','polska']
#xTickMarks = ['jig','hornpipe','polka','reel','slide']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=45, fontsize=10)

## add a legend
#ax.legend( (rects1[0], rects2[0]), ('Input Swedish Tunes', 'Generated Swedish Tunes') )
#ax.legend( (rects1[0], rects2[0]), ('Input Irish Tunes', 'Generated Irish Tunes') )
ax.legend( (rects1[0], rects2[0]), ('Input French Tunes', 'Generated French Tunes') )

plt.show()
