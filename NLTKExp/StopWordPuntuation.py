from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import WordPunctTokenizer

english_stopword = set(stopwords.words('english')+list(punctuation))
sentence ='You can\'t do that! This is a passenger train...The blood of Jesus Christ! You can\'t do that; this is a passenger train! You need to find Jesus!...That is the devil\'s drink. By the blood of Jesus you need to repent!'
sentence ='Alexa can you please turn on the lights of bedroom.'
tokenizer= WordPunctTokenizer()
wordList = tokenizer.tokenize(sentence)

withoutStopword = [word for word in wordList if word not in english_stopword]

print(withoutStopword)