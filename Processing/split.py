# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:23:25 2016

@author: kshtz
"""

from matplotlib import pyplot
import numpy
import random

data_irish=[]
data_swedish=[]
f = open("G:\outputD.txt")
out = open("G:\output_irishD.txt",'w')
out2 = open("G:\output_swedishD.txt",'w')

append = 0
for line in f:
    if "irish" in line or "swedish" in line:
        continue
    if line.startswith("---"):
        append=1-append
    if append==0:
        out.write(line)
    else :
       out2.write(line)
 
out.close()       
out2.close()