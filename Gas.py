import requests
import urllib.request
import time
import pandas as pd
from bs4 import BeautifulSoup

#gas prcies near me
url = 'https://www.autoblog.com/66801-gas-prices/'

#connect to url and print if connected successfully.
response = requests.get(url)
print(response)

#stores html and save bs4 objs.
soup = BeautifulSoup(response.text, "html.parser")


# to download all data, this will loop through all a tags.
soup.findAll('li', class_='shops')
one_li_tag, one_lil_tag, one_il_tag = soup.findAll('ul' class_='details')
link = one_li_tag =['slab price']
link1 = one_lil_tag =['name']
link2 = one_il_tag =['distance']
download_url = 'https://www.autoblog.com/66801-gas-prices/'+ link + link1 + link2
urllib.request.urlretrieve(download_url,'./''link[link.find('/66801-gas-prices/')+1:])
time.sleep(3)
#for i in range(572,len(soup.findAll('<li class="shops">'))):
    #one_a_tag = soup.findAll('"value"')[i]
   # link = one_li_tag['<ul class="details">']
   # link1 = two_li_tag['name']
    #download_url = '/66801-gas-prices/'+ link + link1
  #  urllib.request.urlretrieve(download_url, './'+link[link.find('/66801-gas-prices/'):])
   # time.sleep(5) #pauses so i dont get banned or whatevrrs

#below code is useless



#end uselessness
#the function "main()" makes the scraped data in the Gas station get printed onto a .txt file. If there is not one there, it is instead created. SIDE NOTE: As of now it prints the WHOLE html doc :/..
def main():


    f = open("GasStationPrices.txt", "a+")
   
    for i in range(1):
       f.write(str(soup.prettify()))
   
    f.close()



if __name__== "__main__":
    main()
