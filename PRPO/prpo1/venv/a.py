from pycorenlp import StanfordCoreNLP as NLP_Engine

# Server wrapper
nlp_wrapper = NLP_Engine('http://localhost:80')

# Initial doc
input = "Ronaldo has moved from Real Madrid to Juventus. While messi still plays for Barcelona"
annotators = nlp_wrapper.annotate(input,
    properties={
        'annotators': 'ner, pos',
        'outputFormat': 'json',
        'timeout': 1000,
    })

# Lemmatization
for sentence in annotators["sentences"]:
    for word in sentence["tokens"]:
        print(word["word"] + " => " + word["lemma"])

# POS Tagging
for sentence in annotators["sentences"]:
    for word in sentence["tokens"]:
        print (word["word"] + "=>" + word["pos"])

# NER
for sentence in annot_doc["sentences"]:
    for word in sentence["tokens"]:
        print (word["word"] + "=>" + word["ner"])