import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#gas prcies near me
url = 'https://www.autoblog.com/66801-gas-prices/'

#connect to url and print if connected successfully.
response = requests.get(url)
print(response)

#stores html and save bs4 objs.
soup = BeautifulSoup(response.text, "html.parser")


# to download all data, this will loop through all a tags.
for i in range(572,len(soup.findAll('a'))+1):
    one_a_tag = soup.findAll('a')[i]
    link = one_li_tag['href']
    download_url = ''+ link
    urllib.request.urlretrieve(download_url, './'+link[link.find('/66801-gas-prices/')+1:])
    time.sleep(1) #pauses so i dont get banned or whatevrrs
#soup.findAll('<a>')
#one_li_tag = soup.findAll('<a>')[572]
#link = one_li_tag =['href']
#download_url = 'https://www.autoblog.com/66801-gas-prices/'+ link
#urllib.request.urlretrieve(download_url,'./''link[link.find('/66801-gas-prices/')+1:])
#time.sleep(1)
print(soup)

