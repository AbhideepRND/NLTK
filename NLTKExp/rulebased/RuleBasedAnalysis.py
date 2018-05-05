from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

class ReadWashingtonTimesArticle(object) :

    def parseArticle(self, url):
        page=request.urlopen(url).read().decode('utf8','ignore')
        soup=BeautifulSoup(page,'lxml')
        # map() function returns a list of the results after applying the given function to each item
        # map(fun, iter)
        text=''.join(map(lambda p:p.text, soup.find_all('article')))
        replace = str.encode(text,'ascii',errors='replace')
        return replace.decode().replace('?',' ')

    def generateWordStream(self, text):
        stop_char = set(stopwords.words('english') + list(punctuation))
        wordList = word_tokenize(text.lower())
        return [word for word in wordList if word not in stop_char]

    def summary(self, text, wordList, lines ):
        word_rank = FreqDist(wordList)
        selective_word = nlargest(10,word_rank, key=word_rank.get)
        sentence = sent_tokenize(article)
        ranking = defaultdict(int)
        for index, line in enumerate(sentence):
            for w in word_tokenize(line.lower()):
                if w in selective_word:
                    ranking[index] += word_rank[w]
        line = nlargest(lines,ranking,key=ranking.get)
        return [sentence[j] for j in sorted(line)]

url_artical='https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?noredirect=on&utm_term=.c524f177eaae'
#url_artical='https://www.washingtonpost.com/news/the-switch/wp/2018/05/02/cambridge-analytica-shuts-down-amid-scandal-over-use-of-facebook-data'

washingtonArt = ReadWashingtonTimesArticle()
article = washingtonArt.parseArticle(url_artical)
wordList = washingtonArt.generateWordStream(article)
print(wordList)
print(washingtonArt.summary(article,wordList,4))