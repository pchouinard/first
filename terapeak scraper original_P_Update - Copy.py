import urllib.request
import urllib.parse
import requests
from requests import session

##Usman M.....and Patrick C. 
##9/10/14
##Project Name: Terapeak Scraper


payload = {
    'action': 'login',
    'username': 'webmaster@techtwurl.com',
    'password': 'twurlworld1'
}


with session() as c: #Create a cookie session to login to the protected page
    page_offset = 0 
    result_list = []
    c.post('https://data.terapeak.com/verify/', payload)
    while page_offset <= 50:
        url = "http://data.terapeak.com/?id=0&search=1&view=item_browse&query=iphone+5c&date=2014-09-31&date_range=3&buyer_country_id=1&condition=rollup_3&type%5Bfixed%5D=1&from_start_price=100&to_start_price=1000&from_end_price=100&to_end_price=1000&seller_country_id=1&numPages=18&siteID=0&offset={0}".format(page_offset)
        #print (url)
        request = c.get(url)
        #print (request.headers)
        #print (request.text)

        if not request.ok:
                print ("error")
                # Something went wrong

        for block in request.iter_content(1024):
                if not block:
                        break
                        
                result_list.append(block)
        page_offset += 25
        #print (page_offset)
        #print (result_list)
        end_data = ','.join([i.decode() for i in result_list])
        
    with open("baby.txt", 'w') as text_file:
        text_file.write(end_data.strip())
    
    

print ("It's done d00dz, 1337 pwn sauce hax0r")
			
