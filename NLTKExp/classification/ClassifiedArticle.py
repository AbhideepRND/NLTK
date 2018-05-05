from urllib import request
from bs4 import BeautifulSoup
import math
import re

class Classification(object):

    def checknum(self, val):
        try:
            return int(val)
        except ValueError:
            return 0

    def readLinks(self, url):
        page = request.urlopen(url).read().decode('utf8','ignore')
        soup=BeautifulSoup(page,'lxml')
        pageNo = {self.checknum(j.text):j['href'] for j in soup.findAll('a', {'class':'page-numbers'})}
        max1 = max(pageNo)
        #subdomain = re.search(url+'(.+?)'+str(max1),re.search('href=\"(.+?)\"',str(pageNo[max1])).group(1)).group(1)
        subdomain = re.search(url+'(.+?)'+str(max1),str(pageNo[max1])).group(1)
        print(subdomain)
        urllist = [subdomain+str(i) for i in range(2, max1)]
        return urllist

    def retrievepost(self, url):
        page = request.urlopen(url).read().decode('utf8','ignore')
        soup=BeautifulSoup(page,'lxml')
        return list(map(lambda p:self.replacemulchar(p.text,'','?','\n','\t','\r') ,soup.findAll('div', {'class':'lattest_box_con'})))
        #return [j.text for j in soup.findAll('div', {'class':'lattest_box_con'})]

    def replacemulchar(self, val,  replaceval, *charlist):
         s = str.encode(val,'ascii',errors='replace').decode()
         for i in charlist:
            s = s.replace(i,replaceval)
         return s


clasify = Classification()
url = 'https://www.makingdifferent.com'
url_list = clasify.readLinks(url)

post =[]
post += clasify.retrievepost(url)
for i in range (0,2):
    post += clasify.retrievepost(url+url_list[i])
print(post)

#s ='If you want to invest in cryptocurrencies,? one way to do? that \n \t is through a bitcoin IRA. Once you have done all you need to do, including finding a custodian, you'
#s = str.encode(s,'ascii',errors='replace').decode()
#for i in ['?','\n','\t']:
#    s=s.replace(i,'')

#print(s)