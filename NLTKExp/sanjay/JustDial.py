from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class JustDial(object):

    def __init__(self):
        self.url = "http://www.justdial.com"
        self.urlMap = [];
        self.nextURL =None;


    def parseCityData(self, board, list_of_city):
        self.CityName = ''
        self.CategoryName = ''
        self.PageNr = ''

        for city in list_of_city:
            self.file = open('/home/liveyoung/Tensor/' + city + '.txt', 'w')
            url_comp = self.url + '/' + city+ '/' + board
            self.CityName = city
            self.populateSchoolUrls(url_comp)
           # self.extractSchoolDetails()
            self.file.close();

    def populateSchoolUrls(self, url_comp):
        req = Request(url_comp, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read().decode('utf8', 'ignore')
        soup = BeautifulSoup(page, 'lxml')
        self.nextURL =soup.find('div', {'class', 'jpag'}).find('a', {'rel': 'next'}).get('href')
        print(self.nextURL)
        sectionList = soup.findAll('section', {'class', 'jcar'})
        for section in sectionList:
            self.urlMap.append(section.find('span', {'class', 'jcn'}).find('a').get('href'));

        if self.nextURL != None:
            self.populateSchoolUrls(self.nextURL);

    #School Name#~#Address#~#Contact Person#~#MobileNo#~#Email#~#website#~#Services#~#Link
    def extractSchoolDetails(self, url):
       # for url in self.urlMap:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read().decode('utf8', 'ignore')
        soup = BeautifulSoup(page, 'lxml')
        print(soup.find('div',{'class','company-details'}).find('span',{'class','fn'}).text)
        print(soup.find('span',{'class','telCntct'}).text)
        print(soup.find('span',{'id','adrstxtr'}).text)
        print(soup.find('span',{'class','showmore'}).text)
        tmp= soup.find('i',{'class','web_ic'})
        print(tmp.parent.text if (tmp != None and tmp.parent.name == 'li') else '')




board ="Pre-Schools"

city=['Kolkata']

sulekha = JustDial()
#sulekha.parseCityData(board,city)
sulekha.extractSchoolDetails('https://www.justdial.com/Kolkata/Mount-Litera-Zee-School-DHR-Near-Bishnupu-Joka/033PXX33-XX33-180409171230-J7I3_BZDET?xid=S29sa2F0YSBQcmUgU2Nob29scw==')