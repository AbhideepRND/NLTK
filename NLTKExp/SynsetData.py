from nltk.corpus import wordnet

syn = wordnet.synsets('cookbook')[0]
print(syn.name())
print(syn.definition())
print(syn.examples())
lemmas = syn.lemmas()
for lem in lemmas:
    print(lem)
    print(lem.name())
print(lemmas[0].synset() == lemmas[1].synset())

synonyms =[]
synname=[]
for syn in wordnet.synsets('book'):
    synname.append(syn.name())
    for lem in syn.lemmas():

        synonyms.append(lem.name())

print(synname)
print(synonyms)


book = wordnet.synsets('book')[0]
print(book.hypernyms())
print(book.hypernyms()[0].hyponyms())

## Trying to figure out the word similarity between 'book' and cookbook

syncook = wordnet.synsets('cookbook')[0]
synbook = wordnet.synsets('book')[0]

print(synbook.wup_similarity(syncook))

ref = syncook.hypernyms()[0]