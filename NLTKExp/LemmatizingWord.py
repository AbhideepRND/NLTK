from nltk.stem import WordNetLemmatizer
lemmatizer =  WordNetLemmatizer()

print(lemmatizer.lemmatize('studied')) # By default it return the noun phase
print(lemmatizer.lemmatize('studied', pos='v'))