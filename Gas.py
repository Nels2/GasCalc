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
for i in range(572,len(soup.findAll('<li class="shops"'))):
    one_a_tag = soup.findAll('value')[i]
    link = one_li_tag['<ul class="details"']
    link1 = two_li_tag['name']
    download_url = '/66801-gas-prices/'+ link + link1
    urllib.request.urlretrieve(download_url, './'+link[link.find('/66801-gas-prices/'):])
    time.sleep(1) #pauses so i dont get banned or whatevrrs

#below code is useless

#soup.findAll('<a>')
#one_li_tag = soup.findAll('<a>')[572]
#link = one_li_tag =['href']
#download_url = 'https://www.autoblog.com/66801-gas-prices/'+ link
#urllib.request.urlretrieve(download_url,'./''link[link.find('/66801-gas-prices/')+1:])
#time.sleep(1)

#end uselessness
#the function "main()" makes the sraped data in the Gas station get printed onto a txt file. if there is not one there it is instead created. as of now it prints the WHOLE html doc..
def main():


    f = open("GasStationPrices.txt", "a+")
   
    for i in range(10):
       f.write(str(soup.findAll))
   
    f.close()



if __name__== "__main__":
    main()
