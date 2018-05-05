from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize

from nltk.corpus import webtext

text = webtext.raw('overheard.txt')
sent_tokenizer = PunktSentenceTokenizer(text)
sents1 = sent_tokenizer.tokenize(text)
print(sents1[678])

sents2= sent_tokenize(text)
print(sents2[678])

with open('D:\Python\Data\overheard.txt',encoding='ISO-8859-2') as f:
    text2 = f.read()

sent_tokenizer3 = PunktSentenceTokenizer(text2)
sents3 = sent_tokenizer3.tokenize(text)
print(sents3[0])