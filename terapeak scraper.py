import urllib.request
import urllib.parse

username = "webmaster@techtwurl.com"
password = "twurlworld1"
url = 'http://data.terapeak.com/?id=0&search=1&view=item_browse&query=iphone+4&date=2013-10-24&date_range=4&buyer_country_id=1&condition=rollup_3&type%5Bfixed%5D=1&from_start_price=50&to_start_price=350&from_end_price=50&to_end_price=550&seller_country_id=1&txn_site_id=0&numPages=50&siteID=0&offset=200'
values = { 'username': username,'password': password }
data = urllib.parse.urlencode(values)
binary_data = data.encode('ASCII')
req = urllib.request.Request(url, binary_data)
response = urllib.request.urlopen(req)
result = response.read()
print (result)








##from urllib.request import urlopen
##import urllib.request
##
### create a password manager
##password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
##username = "webmaster@techtwurl.com"
##password = "twurlworld1"
##
### Add the username and password.
### If we knew the realm, we could use it instead of None.
##top_level_url = "https://data.terapeak.com/verify/?url=%2F%3F_ga%3D1.96593055.1821241052.1410315918"
##password_mgr.add_password(None, top_level_url, username, password)
##
##handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
##
### create "opener" (OpenerDirector instance)
##opener = urllib.request.build_opener(handler)
##
### use the opener to fetch a URL
##a_url = "http://data.terapeak.com/?id=0&search=1&view=item_browse&query=iphone+4&date=2013-10-24&date_range=4&buyer_country_id=1&condition=rollup_3&type%5Bfixed%5D=1&from_start_price=50&to_start_price=350&from_end_price=50&to_end_price=550&seller_country_id=1&txn_site_id=0&numPages=50&siteID=0&offset=200"
##data1 = opener.open(a_url)
##
### Install the opener.
### Now all calls to urllib2.urlopen use our opener.
##urllib.request.install_opener(opener)
##print (data1)
##output = open('terapeak.txt','wb')
##output.write(data1.read())
##output.close()
