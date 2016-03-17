# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:43:05 2016

@author: kshtz
"""

from music21 import *
import base64

s = converter.parse('G:\\french.abc')
mf = midi.translate.streamToMidiFile(s)
#mf.open('G:\\irish.midi', 'wb')
print(mf.writestr()) 
#mf.write()
#mf.close()  
#f = open('G:\\irish.midi', 'rb').readlines()
string="data:audio/mid;base64,"
f=open('G:\\french.mid','w')
f.write(string)
f.close()
out = open("G:\\french.mid",'ab')
out.write(base64.b64encode(mf.writestr()))
out.close()



