import nltk
import nltk.stem as stemmer

import pandas as pd
from nltk.corpus import stopwords
from gensim.corpora import Dictionary
from gensim.test.utils import get_tmpfile
import gensim
from gensim import corpora
from pprint import pprint
from gensim.utils import simple_preprocess
from smart_open import smart_open
import os
from gensim.parsing.preprocessing import remove_stopwords

#data = pd.read_csv("science.csv")

x=pd.read_csv("science.csv")

X=[]
for i, row in x.iterrows():
        X.append(row['body_no_quote'])
       
from nltk.stem import WordNetLemmatizer
import re
stemmer = WordNetLemmatizer()
documents=[]
print(remove_stopwords("the hair it is good us"))
for sen in range(0, len(X)):
    # Remove all the special characters
    print(X[sen])
    document = re.sub(r'\W', ' ', str(X[sen]))
    print(document)
    document=document.lower()
    
    #print(document)
    
        
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
    
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    
    # Converting to Lowercase
    document = document.lower()
    document=remove_stopwords(document)
    # Lemmatization
    document = document.split()
    
    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    
    documents.append(document)      

'''
documents = list(dict.fromkeys(documents))
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents).toarray()
'''
stop_words = set(stopwords.words('english'))
texts = [[text for text in doc.split()] for doc in documents]
for i in texts:
    for j in i:
        if j in stop_words:
            i.remove(j)
            
        
dictionary = corpora.Dictionary(texts)
print(dictionary)
tokenized_list = [simple_preprocess(doc) for doc in documents]

mydict = corpora.Dictionary()
mycorpus = [mydict.doc2bow(doc, allow_update=True) for doc in tokenized_list]

matrix=[]
#Y=[]
#Y.extend(matrix)

for i in range(len(mycorpus)):
    word=[]
    count=[]
    temp=[]
    for tu in mycorpus[i]:
        
        word.append(tu[0])
        count.append(tu[1])
        #print(word,count)
    for j in range(0,2912):
        if j in word:
            temp.append(count[word.index(j)])
        else:
            temp.append(0)
    matrix.append(temp)
vocab=tuple(mydict.token2id.keys())
print("HI")


seed_topic_list = [['removed', 'remove', 'banned', 'ban', 'warned', 'spam'],
               ['recommend', 'look', 'try']]