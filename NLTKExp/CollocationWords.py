from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
import nltk.data



tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
para = "Hello World. It's good to see you. Thanks for buying this book."
token2 = tokenizer.tokenize(para)
print(token2)
word = [];
tree = TreebankWordTokenizer()


for sent in token2:
    word.append(tree.tokenize(sent))


print(word)


print(word_tokenize("can't"))