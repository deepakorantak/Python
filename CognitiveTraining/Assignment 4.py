import nltk
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from gensim import corpora, models

_files_all_speechs = state_union.fileids()
all_raw_speeches = []
for _file_ in _files_all_speechs:
    all_raw_speeches.append(state_union.raw(_file_))

#print('Number of Speeches:', len(all_raw_speeches))
all_categories = [x.split('-')[1].split('.')[0] for x in _files_all_speechs]
#print(all_categories)


stopwords = nltk.corpus.stopwords
eng_stopwords = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()

def basic_preprocessing(text):
    text = text.lower() #lowering
    text = re.sub(r'\[.*?\]', '', text) #removing all instances of citation brackets found in wiki articles
    text = word_tokenize(text)
    text = [word for word in text if word not in eng_stopwords] #removing stop words
    text = [word for word in text if len(word) > 1] #removing single character tokens
#     text = [wordnet_lemmatizer.lemmatize(word) for word in text]

    return(text)
processed_texts = [basic_preprocessing(text) for text in all_raw_speeches]

#print(processed_texts)

## Creating all {index:word} relations
dictionary = corpora.Dictionary(processed_texts)
# for key in dictionary.iterkeys():
#     print(key,dictionary[key])

# ## Converting corpus to a list of indices
corpus = [dictionary.doc2bow(text) for text in processed_texts]
#print(corpus[1])

# ## Initializing TFIDF parameters from corpus
tfidf = models.TfidfModel(corpus)

# ## Creating TFIDF Matrix from data
corpus_tfidf = tfidf[corpus]
print(corpus_tfidf.obj)

 ## Creating LSA model on the tfidf
lsi = models.LsiModel(corpus_tfidf, id2word = dictionary, num_topics = 120)
lsi.print_topics(10)

lsi_corpus = []
for lsi_doc in lsi[corpus]:
    lsi_corpus.append([topic_component[1] for topic_component in lsi_doc])
import numpy as np
lsi_corpus = np.array(lsi_corpus)
print(lsi_corpus.shape)


from sklearn.naive_bayes import BernoulliNB
nb_model = BernoulliNB()
nb_model.fit(lsi_corpus, all_categories)


from sklearn.metrics import accuracy_score

#backslash means the function continues in next line\
print('Accuracy on test data: {}%'.format(\
                                          accuracy_score(all_categories, nb_model.predict(lsi_corpus))\
                                          *100))