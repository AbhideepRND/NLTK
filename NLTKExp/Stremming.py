from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))
