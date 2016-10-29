#!/usr/bin/env python
import urllib.request
import urllib.parse
import requests
import csv
from requests import session
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

payload = {
    'action': 'login',
    'username': 'webmaster@techtwurl.com',
    'password': 'twurlworld1'
}

page_offset = 0
date = 1
result_list = []
listof_listof_lists= []
z = {}

def cookie(date, page_offset, payload):
    
    """ this creates a cookie session so we can iterate
    through multiple urls without having to login into the account every time """
    
    print("cookie")
    
    with session() as c: #Create a cookie session to login to the protected page 
        c.post('https://data.terapeak.com/verify/', payload)
        url = "http://data.terapeak.com/?id=0&search=1&view=item_browse&query=iphone+4s&date=2014-12-1&date_range=1&buyer_country_id=1&condition=rollup_3&type%5Bfixed%5D=1&from_start_price=100&to_start_price=800&from_end_price=100&to_end_price=800&seller_country_id=1&txn_site_id=0&numPages=12&siteID=0&offset={25}"
        date_setup(date, page_offset, url,c)

#next set the date and then the page offset
        
def date_setup(date, page_offset, url,c):
    
    """ check the date 'date=2014-09-1' and see if it needs to be updated, if not
    we are done and the month needs to be updated to date=2014-10-1  """

    if date <= 31:
        page_offset = 0
        url = "http://data.terapeak.com/?id=0&search=1&view=item_browse&query=iphone+4s&date=2014-12-1&date_range=1&buyer_country_id=1&condition=rollup_3&type%5Bfixed%5D=1&from_start_price=100&to_start_price=800&from_end_price=100&to_end_price=800&seller_country_id=1&txn_site_id=0&numPages=12&siteID=0&offset={0}".format(page_offset)
        u = list(url)
        new = str(date)
        u[86] = new #this will update the date from date=2014-09-1 to date=2014-09-2
        date_ed_url = "".join(u)
        #print(edited)
        page_offset_update(date, page_offset, date_ed_url, c) # the date has now been updated and the page_offset has been reset to 0
    else:
        with open("4s_test_Dec_2014_.csv", "w", newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerows(listof_listof_lists)
            print("done")
            quit



def page_offset_update(date, page_offset, date_ed_url, c):
    
    """ update the page_offset, if the offset exceeds 300,
    send it to be refreshed and given a new date update. I had to use this
    stupid string to list to string formatting, but it works"""

    if page_offset <= 300:
        if date <=9:
            pg_list = list(date_ed_url)
            new = list(str(page_offset))
            better = pg_list[0:295] + new #this will update the page_offset from 25 to 50 and so on until it hits 300
            date_ed_url = "".join(better)
            print(date_ed_url)
            machine(date, page_offset, date_ed_url, c)
        else: 
            pg_list = list(date_ed_url)
            new = list(str(page_offset))
            better = pg_list[0:296] + new #this will update the page_offset from 25 to 50 and so on until it hits 300
            date_ed_url = "".join(better)
            print(date_ed_url)
            machine(date, page_offset, date_ed_url, c)
    else:
        date += 1
        date_setup(date, page_offset, date_ed_url, c) #the page_offset is now > 300, go up to date_setup to adjust the date


def machine(date, page_offset, date_ed_url, c):
    
    """ we iterate through the row-dark tag and put everything into a list which is then written into CSV """

    print("me machine")
    request = c.get(date_ed_url)
    r = request.text
    
    
    #print(r)
    if not request.ok:
        print ("error")
    # Something went wrong

    soup = BeautifulSoup(r)
    
    linkss=soup.find_all("tr",{"class":"row-dark"})     
    tup_list = []
    unit_listt = []
    

    for i in linkss[0:-1]: #there is an empty list at the end for some reason...still needs to be checked
        unit = []
        i = str(i)

       #D soup is for description, a is the anchor

        D_soup=BeautifulSoup(i)
        x = D_soup.find_all("a")[0]
        #d[x.get_text()] = tuple()
        title_key = x.get_text()
        unit.append(title_key)
        #print(title_key)

       #items is grabbing the prices

        items=D_soup.find_all("td",{"class":"sorted"})
        if items != []:
            item_1 = items[0]
            xx = item_1.get_text()
            unit.append(xx)
            #print("")
            #print(xx[1:])
       
       #dates is grabbing the END date for the listing
       
        dates=D_soup.find_all("td",{"class":"last-child"})
        if items != []:
            date_1 = dates[0]
            xxx = date_1.get_text()
            unit.append(xxx)
            #print(xxx)
            
        unit_listt.append(unit)
        listof_listof_lists.append(unit)
        tupp_ = (xx, xxx)
        tup_list.append(tupp_)
        #print('')

       #no longer using a dict, so its commented out below
        #title_key = x.get_text()
        cnt = len(tup_list)
        for j in range(cnt):
            z[title_key] = tup_list[j]

    #page_offset += 25
    print("round complete")
    print()
    print()
    print(len(unit_listt))
    print(unit_listt) #list of each individual page listings 
    
    #the difference between unit_list and listof_listof_lists is that unit_list is a list of the individual session and
    #listof_listof_lists is a list of every session or "page". So if page_offset is on 75, at this location of the code, unit_list
    # is equal to 25 listings and listof_listof_lists is equal to 75 listings. Because each page has 25 listings, if unit_list is ever less than
    #25 it means we have reached the last page of the url (so the date now needs to be updated)
    
##    with open("clayton_writing_.csv", "w", newline='', encoding='UTF-8') as f:
##        writer = csv.writer(f)
##        writer.writerows(listof_listof_lists)

    if len(unit_listt) < 5:
        print("here, update below")
        print()
        page_offset += 378
        page_offset_update(date, page_offset, date_ed_url, c)

    else:
        print("not yet")
        page_offset += 25
        page_offset_update(date, page_offset, date_ed_url, c)
   

    
def main():
    """ this starts the process """
    
    cookie(date, page_offset, payload)

main()
