# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 13:09:38 2016

@file crd.py
@author: Apurva Pathak
@brief Program to scrape data from Amazon.
"""

import time
import urllib2
import pickle
import string

from bs4 import BeautifulSoup

BASE_URL='http://www.lotro-abc.com/'
song_list='songlist.html'
genre=['rock','classical','video','metal']
music=[[] for g in genre]

fname=urllib2.urlopen(BASE_URL+song_list)
soup=BeautifulSoup(fname,"html.parser")
tbl=soup.find_all("table")
row=tbl[1].find_all("tr")

max_row=10000000000

for i in range(1,min(len(row),max_row)):
    print i
    td=row[i].find_all("td")
    links=td[2].find_all('a')
    for link in links:
        song_link=str(link['href'])
        if('.abc' in song_link):
            for j,g in enumerate(genre):
                if(g in string.lower(str(td[3].get_text()))):
                    while True:
                        try:
                            f=urllib2.urlopen(BASE_URL+song_link)
                            s=BeautifulSoup(f,"html.parser")
                            song=s.get_text()
                            song=song.replace('  ','')
                            song=''.join([i if ord(i) < 128 else ' ' for i in song])
                            song = song.decode("utf-8-sig").encode("utf-8")
                            music[j].append(song)
                            break
                        except:
                            print song_link
                            print 'trying again'
                
for i,m in enumerate(music):
    fname=open(genre[i]+'.txt','w')
    for song in m:
        fname.write('<start>\n')
        fname.write(song)
        fname.write('\n<end>\n')
    fname.close()