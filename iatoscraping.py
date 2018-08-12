# -*- coding: utf-8 -*-
"""
Created on Sun May 20 08:22:41 2018

@author: Arjun
"""
import re
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
response = urlopen("http://www.iato.in/members/lists")
page_source = response.read()
d=page_source.decode("windows-1252")
i=d.find('<table')
j=d.find('</table')
d=d[i:j]
d=BeautifulSoup(d,"lxml")
url=[]
for link in d.findAll('a'):
    url.append(link.get('href'))
i=0
column=['Company Name','Contact Person','Designation','Address','City','State','Pincode','Email','Phone','Mobile','Fax','Website']
with open("output1.csv",'a',newline="") as resultFile:
     wr = csv.writer(resultFile, dialect='excel')
     wr.writerow(column)
for x in url:
    response = urlopen(x).read()
    d[i]=response.decode("utf-8")
    k=d[i].find('<div class="post-content"')
    d[i]=d[i][k:]
    j=d[i].find('END / POST ')
    d[i]=BeautifulSoup(''.join(d[i][:j]),"lxml")
    d[i]=d[i].text
    j=d[i].find('Name of the Company')
    d[i]=d[i][j:]
    pattern=re.compile( r":.*")
    d[i]=re.findall(pattern,d[i])
    d[i]=[s[2:] for s in d[i]]
    with open("output.csv",'a',newline="") as resultFile:
     wr = csv.writer(resultFile, dialect='excel')
     wr.writerow(d[i])
    i=i+1