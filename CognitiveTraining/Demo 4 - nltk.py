import nltk, re

sample_text = "I'm employee of Microsoft. Microsoft was established in 1943."
sentences = nltk.sent_tokenize(sample_text)
tokenized_sentences = []

for sentence in sentences:
    tokenized_sentences.append(nltk.word_tokenize(sentence))

pos_tags = []
for tokenized_sentence in tokenized_sentences:
    pos_tags.append(nltk.pos_tag(tokenized_sentence))

ne_chunks = []
for pos_tag_sentence in pos_tags:
    ne_chunks.append(nltk.ne_chunk(pos_tag_sentence, binary = False))

print(pos_tags)
print(ne_chunks)

def get_entities(text):
    corpus_clean = re.sub("[^a-zA-Z\s\.\']", ' ', text) #Replace any character which is not an alphabet or ' ' (space) or '.' or apostrophe "'" with space
    sentences = nltk.sent_tokenize(corpus_clean)
    sentences_ = [nltk.word_tokenize(sent) for sent in sentences]
    sentences_ = [nltk.pos_tag(sent) for sent in sentences_] # POS Tagging each word-tokenized sentence separately
    k_tree = [nltk.ne_chunk(sent, binary = False) for sent in sentences_] # Extract Named-Entities on each POS-Tagged Sentence
    
    #########
    #Logic to remove named-entities from k_tree
    entities = [] 
    for tree in k_tree:
        entities_ = []
        for word in tree:
            if isinstance(word[0], tuple):
                entities_.append((word[0][0], word.label()))
        entities.append(entities_)
    #End of loop
    #########
    return entities

trees = get_entities("I'm employee of Microsoft. Microsoft was established in 1943.")

print(trees)
