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
            self.extractSchoolDetails()
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

    def extractSchoolDetails(self):

        for url in self.urlMap:
            finalList = []
            print(url)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(req).read().decode('utf8', 'ignore')
            soup = BeautifulSoup(page, 'lxml')
            finalList.append(soup.find('div',{'class','company-details'}).find('span',{'class','fn'}).text)  #School Name
            finalList.append(''.join(soup.find('span',{'id','adrstxtr'}).text.splitlines()))                #Address
            finalList.append('')
            if soup.find('span', {'class', 'telCntct'}) != None:
                if len(soup.find('span', {'class', 'telCntct'}).find('a').text) < 2:
                    finalList.append(self.extractPhoneNo(soup))
                else:
                    soup.find('span', {'class', 'telCntct'})
                    finalList.append(
                        ';'.join(v[-10:] for v in soup.find('span', {'class', 'telCntct'}).text.strip().split(',')))
            else:
                finalList.append('')
            finalList.append('')                                                                            #Email
            tmp = soup.find('i', {'class', 'web_ic'})
            finalList.append(tmp.parent.text.strip() if (tmp != None and tmp.parent.name == 'li') else '')  #website
            finalList.append(','.join(v.replace('\t','') for v in soup.find('span', {'class', 'showmore'}).text.strip().splitlines())) #Services
            finalList.append(url)
            val = '#~#'.join(str(v) for v in finalList)
            self.file.write(val + '\n')

    def extractPhoneNo(self, data):
        tmp2 = data.findAll('style')
        style = tmp2[1].text
        finalPhone=[]
        phoneNoList = data.find('span',{'class','telCntct'}).find('a').contents
        for span in phoneNoList[4:]:
            if span != ' ':
                label = span.get('class')[1]
                index =style.find(label)+label.__len__()+21
                finalPhone.append(int(style[index:index+2])-1)
        return ''.join(str(v) for v in finalPhone)

'''
    def extractSchoolDetails(self,url):
        finalList = []
        print(url)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read().decode('utf8', 'ignore')
        soup = BeautifulSoup(page, 'lxml')
        finalList.append(soup.find('div',{'class','company-details'}).find('span',{'class','fn'}).text)  #School Name
        finalList.append(''.join(soup.find('span',{'id','adrstxtr'}).text.splitlines()))                #Address
        finalList.append('')                                                                            #Contact Person
        if len(soup.find('span', {'class', 'telCntct'}).find('a').text)<2:
            finalList.append(self.extractPhoneNo(soup))
        else:
            soup.find('span', {'class', 'telCntct'})
            finalList.append(';'.join(v[-10:] for v in soup.find('span', {'class', 'telCntct'}).text.strip().split(',')))
        finalList.append('')                                                                            #Email
        tmp = soup.find('i', {'class', 'web_ic'})
        finalList.append(tmp.parent.text.strip() if (tmp != None and tmp.parent.name == 'li') else '')  #website
        finalList.append(','.join(v.replace('\t','') for v in soup.find('span', {'class', 'showmore'}).text.strip().splitlines())) #Services
        finalList.append(url)
        val = '#~#'.join(str(v) for v in finalList)
        print(val)
'''

board ="Pre-Schools"

city=['Kolkata']

justDial = JustDial()
justDial.parseCityData(board,city)
#justDial.extractSchoolDetails('https://www.justdial.com/Kolkata/Blue-Butterfly-Pre-School-Near-Old-St-Xaviers-Building-Sodepur/033PXX33-XX33-170919152844-Q7A1_BZDET?xid=S29sa2F0YSBQcmUgU2Nob29scw==')

#https://www.justdial.com/Kolkata/Kidzee-Habra/9999PXX33-XX33-170113124959-Y7C3_BZDET?xid=S29sa2F0YSBQcmUgU2Nob29scw==
#https://www.justdial.com/Kolkata/Blue-Butterfly-Pre-School-Near-Old-St-Xaviers-Building-Sodepur/033PXX33-XX33-170919152844-Q7A1_BZDET?xid=S29sa2F0YSBQcmUgU2Nob29scw==
#https://www.justdial.com/Kolkata/Aptech-Montana-International-Preschool-Behind-Coal-Bhawan-New-Town/033PXX33-XX33-180326150150-F4M7_BZDET?xid=S29sa2F0YSBQcmUgU2Nob29scw==