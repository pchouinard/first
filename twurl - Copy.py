#!/usr/bin/env python

#import urllib.parse
#import urllib.requests
#import requests
from bs4 import BeautifulSoup
#from collections import OrderedDict


f=open('out_test.txt','r')
#contents = f.read()
##print(type(contents))

soup = BeautifulSoup(f.read(), 'html.parser')


#print(soup.get_text())
#print(soup.name)
#div class='tt-main'


z = {}

linkss=soup.find_all("tr",{"class":"row-dark"})     #print(linkss)

#print(linkss)
tup_list = []

for i in linkss[0:-1]: #there is an empty list for some reason
     i = str(i)


     #D soup is for description, a is the anchor

     D_soup=BeautifulSoup(i)
     x = D_soup.find_all("a")[0]
     #d[x.get_text()] = tuple()
     title_key = x.get_text()
     print(title_key)

     #items is grabbing the prices

     items=D_soup.find_all("td",{"class":"sorted"})
     if items != []:
          item_1 = items[0]
          xx = item_1.get_text()
          
          #print("")
          print(xx[1:])
     
     #dates is grabbing the END date for the listing
     
     dates=D_soup.find_all("td",{"class":"last-child"})
     if items != []:
          date_1 = dates[0]
          xxx = date_1.get_text()
          print(xxx)
     tupp_ = (xx, xxx)
     tup_list.append(tupp_)
     print('')

     #create eer-thing
     #title_key = x.get_text()
     cnt = len(tup_list)
     for j in range(cnt):
          z[title_key] = tup_list[j]


print('')
#print(list(d.items())[0])

print(z)




############################
#trying this on the original
############################
          
##linkss=soup.find_all("tr",{"class":"row-dark"})
##
###print(linkss)
##tup_list = []
##
##for i in linkss[0:-1]:
##     i = str(i)
##
##
##     #D soup is for description, a is the anchor
##
##     D_soup=BeautifulSoup(i)
##     x = D_soup.find_all("a")[0]
##     #d[x.get_text()] = tuple()
##     title_key = x.get_text()
##     print(title_key)
##
##     #items is grabbing the prices
##
##     items=D_soup.find_all("td",{"class":"sorted"})
##     if items != []:
##          item_1 = items[0]
##          xx = item_1.get_text()
##          
##          #print("")
##          print(xx[1:])
##     
##     #dates is grabbing the END date for the listing
##     
##     dates=D_soup.find_all("td",{"class":"last-child"})
##     if items != []:
##          date_1 = dates[0]
##          xxx = date_1.get_text()
##          print(xxx)
##     tupp_ = (xx, xxx)
##     tup_list.append(tupp_)
##     print('')
##
##     #create eer-thing
##     #title_key = x.get_text()
##     cnt = len(tup_list)
##     for j in range(cnt):
##          d[title_key] = tup_list[j]
##
##
##print('')
###print(list(d.items())[0])
##
##print(d)    
##          








 


























