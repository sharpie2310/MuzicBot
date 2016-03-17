# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:23:59 2016

@author: kshtz
"""

from matplotlib import pyplot
import numpy
import random
from collections import defaultdict

def processFile(file):
    rythm = set()
    keys = set()
    keysCount=defaultdict(int)
    rythmCount=defaultdict(int)
    f = open(file)
    for line in f:
        if line.startswith("R:"):
            rythm.add(line.strip().split(":")[1])
            if line.strip().split(":")[1] in rythmCount:
                rythmCount[line.strip().split(":")[1]]+=1
            else :
                rythmCount[line.strip().split(":")[1]]+=1
        if line.startswith("K:"):
            keys.add(line.strip().split(":")[1])
            if line.strip().split(":")[1] in keysCount:
                keysCount[line.strip().split(":")[1]]+=1
            else :
                keysCount[line.strip().split(":")[1]]+=1
    f.close()
    return rythm,keys,rythmCount, keysCount

rythmIrish, keysIrish, rythmIrishCount, keysIrishCount = \
        processFile("G://MS/Homework-Q2/cse 253/Project/examples/examples/Data/french_music.txt")
rythmIrishN, keysIrishN, rythmIrishCountN, keysIrishCountN = \
        processFile("G:\output_frenchD.txt")
rythmSwedish, keysSwedish, rythmSwedishCount, keysSwedishCount = \
       processFile("G:\MS\Homework-Q2\cse 253\Project\examples\examples\Data\swedish_music.txt")
rythmSwedishhN, keysSwedishN, rythmSwedishCountN, keysSwedishCountN = \
        processFile("G:\output_swedishD.txt")

print(sum(list(rythmIrishCount.values())))
print(sum(list(rythmIrishCountN.values())))
print([(k, rythmIrishCount[k]) for k in sorted(rythmIrishCount, key=rythmIrishCount.get, reverse=True)][:6])
print([(k, rythmIrishCountN[k]) for k in sorted(rythmIrishCountN, key=rythmIrishCountN.get, reverse=True)][:6])

#print(sum(rythmSwedishCount.values()))
#print(sum(rythmSwedishCountN.values()))
#print([(k, rythmSwedishCount[k]) for k in sorted(rythmSwedishCount, key=rythmSwedishCount.get, reverse=True)][:5])
#print([(k, rythmSwedishCountN[k]) for k in sorted(rythmSwedishCountN, key=rythmSwedishCountN.get, reverse=True)][:5])
'''
def match(tunekeys, regex, files):
    for key in (tunekeys):
        print(key)
        for file in files:
            f = open(file)
            count =0
            for line in f:
                if line.startswith(regex):
                    if key in line.strip().split(":")[1]:
                        count+=1
            f.close()
            print(count)

#match(rythm,"R:", ["G:\output_irishD.txt"])
match(rythmIrish-rythmSwedish,"R:", ["G:\output_irishD.txt","G:\output_swedishD.txt"])
print ("swedish now")
match(rythmSwedish-rythmIrish,"R:", ["G:\output_irishD.txt","G:\output_swedishD.txt"])
'''