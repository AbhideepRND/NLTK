from urllib import request
from bs4 import BeautifulSoup

class ReadSulekha(object):

    def __init__(self):
        self.url="https://www.sulekha.com"
        self.nextPage="/mvc5/lazy/v1/Listing/get-business-list?PartialPageData=#1&PageNr=#2&Sort=&getQuoteVisiblity=&aboutEnabled=&CategoryName=#3CityName=&4&IsAboutEnabled=True"
        self.urlMap = {};

    def parseCityData(self, board, list_of_city):
        self.CityName=''
        self.CategoryName=''
        self.PageNr=''
        for city in list_of_city:
            url_comp=self.url+'/'+board+'/'+city
            self.CityName=city
            page = request.urlopen(url_comp).read().decode('utf8', 'ignore')
            soup = BeautifulSoup(page, 'lxml')
            pageURL = self.url + self.nextPage
            partial = soup.find('input', {'id': 'partialPageData'}).get('value')
            pageURL=pageURL.replace('#1',partial)
            self.CategoryName=soup.find('input',{'id':'hdnSubCategoryName'}).get('value').replace(' ','+')
            pageURL=pageURL.replace('#3', self.CategoryName)
            pageURL=pageURL.replace('#4', self.CityName)
            self.populateSchoolNameAndURL(pageURL)
            self.extractSchoolDetails()

    def populateSchoolNameAndURL(self, pageURL):
        i=1
        while True:
            finalURL = pageURL.replace('#2',str(i))
            print(finalURL)
            page = request.urlopen(finalURL).read().decode('utf8', 'ignore')
            soup = BeautifulSoup(page, 'lxml')
            for schname in soup.find_all('a',{'class':'GAQ_C_BUSL'}):
                self.urlMap[schname.text]=schname.get('href')
            if soup.find('input', {'id': 'hdnBizHasMoreResults'}).get('value') == 'False':
                break;
            i=i+1
    def extractSchoolDetails(self):
        for key,value in self.urlMap.items():
            page = request.urlopen(self.url+value).read().decode('utf8', 'ignore')
            soup = BeautifulSoup(page, 'lxml')
            dataList={}
            dataList["address"]=soup.find('address')
            dataList['contactPerson']=soup.find('label', {'class':'icon-person'})
            dataList['mobileno']=soup.find('span', {'class': 'icon-mobile ph-no'})
            dataList['emailid']=soup.find('label', {'class': 'icon-email'})
            dataList['website']=soup.find('span', {'class': 'busurl'})
            dataList['service']=';'.join(map(lambda p: p.text, soup.find_all('a',{'class':'GAQ_C_SERVICEOFFERED'})))
            for k, const in dataList.items():
                if const != None and isinstance(const,str)==False :
                    print(const.text)


board ="icse-schools"

city=['chennai']

sulekha = ReadSulekha()
sulekha.parseCityData(board,city)
