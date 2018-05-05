import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer

import enchant


replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]


stopword_set = set(stopwords.words('english')+list(punctuation))
lemmatizer = WordNetLemmatizer()

class RegexpReplacer(object):
    def __init__(self, patterns = replacement_patterns):
        self.pattern = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replacer(self ,text):
        s = text
        for (expression, repl) in self.pattern:
            s = re.sub(expression, repl, s)
        return s;


regReplacer = RegexpReplacer()
print(regReplacer.replacer("can't find the word"))
print(regReplacer.replacer("we'll should've find the word"))

# Now we are before tokenizing the word from sentence we replace contraction word.

str="can't find the word."
print(word_tokenize(regReplacer.replacer(str)))

# Step we are following
# 1. replace all the contraction word
# 2. tokenize all the word
# 3. remove stop words
# 4. lematize the words

str="Alexa'll you please turn all the lights on of my bedroom."

wordList= word_tokenize(regReplacer.replacer(str))
print("Printing the word list after contraction =",wordList)
word = [lemmatizer.lemmatize(word) for word in wordList if word not in stopword_set]

print("Printing the word list after removing stop words =",word)