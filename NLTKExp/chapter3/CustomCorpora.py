import nltk.data
from nltk.corpus.reader import WordListCorpusReader
from nltk.corpus import names
from nltk.corpus.reader import TaggedCorpusReader
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import treebank

wordlist = WordListCorpusReader("C:/nltk_data/corpora/cookbook" ,['wordlist'])
print(wordlist.words())
print(wordlist.fileids())

print(names.fileids())
print(len(names.words('male.txt')))

reader = TaggedCorpusReader("C:/nltk_data/corpora/treebank/tagged",r'.*\.pos', word_tokenizer=SpaceTokenizer(), tagset='en-brown')
print(reader.words('wsj_0001.pos'))
print(reader.tagged_words('wsj_0001.pos'))
print(reader.tagged_sents('wsj_0001.pos'))
print(reader.tagged_paras('wsj_0001.pos'))
print(reader.fileids())

print("\n")
print(reader.tagged_words('wsj_0001.pos',tagset='universal'))

print(treebank.tagged_words())