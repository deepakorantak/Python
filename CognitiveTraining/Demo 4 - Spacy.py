import spacy
nlp = spacy.load('en') #loading the language module. 
TEXT = '''Avul Pakir Jainulabdeen Abdul Kalam better known as A. P. J. Abdul Kalam (/ˈæbdʊl kəˈlɑːm/ (About this sound listen); 15 October 1931 – 27 July 2015), was the 11th President of India from 2002 to 2007. A career scientist turned statesman, Kalam was born and raised in Rameswaram, Tamil Nadu, and studied physics and aerospace engineering. 
He spent the next four decades as a scientist and science administrator, mainly at the Defence Research and Development Organisation (DRDO) and Indian Space Research Organisation (ISRO) and was intimately involved in India's civilian space programme and military missile development efforts. 
He thus came to be known as the Missile Man of India for his work on the development of ballistic missile and launch vehicle technology. 
He also played a pivotal organisational, technical, and political role in India's Pokhran-II nuclear tests in 1998, the first since the original nuclear test by India in 1974.'''
doc = nlp(TEXT) #this applies all the common functions that we have studied so far.
print([x for x in doc]) ## Word Tokenizing
print([x for x in doc.sents])  ## Sentence tokenizing
print([(x, x.tag_) for x in doc]) ## POS Tagging
## Names Entities
for x in doc.ents:
    print(x,'---', x.label_)

def extract_currency_relations(doc):
    # merge entities and noun chunks into one token
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    relations = []
    for money in filter(lambda w: w.ent_type_ == 'MONEY', doc):
        if money.dep_ in ('attr', 'dobj'):
            subject = [w for w in money.head.lefts if w.dep_ == 'nsubj']
            if subject:
                subject = subject[0]
                relations.append((subject, money))
        elif money.dep_ == 'pobj' and money.head.dep_ == 'prep':
            relations.append((money.head.head, money))
    return relations

TEXTS = [
    'Net income was $9.4 million compared to the prior year of $2.7 million.',
    'Revenue exceeded twelve billion dollars, with a loss of $1b.',
    'The amount robbed from the bank was 10$'
     ]

print("Processing %d texts" % len(TEXTS))

for text in TEXTS:
    doc = nlp(text)
    relations = extract_currency_relations(doc)
    for r1, r2 in relations:
        print('{:<10}\t{}\t{}'.format(r1.text, r2.ent_type_, r2.text))     