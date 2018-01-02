from textblob import TextBlob
from nltk.corpus import brown as b
import numpy as np


def analysis(text):
    corpus = text.split()
    for i, c in enumerate(corpus):
        corpus[i] = c.lower()
    lower = ' '.join(corpus)
    text = TextBlob(lower)
    for i, t in enumerate(text.words):
        corpus[i] = t.lemma
    lemma = ' '.join(corpus)
    text = TextBlob(lemma)

    brown_words = list(b.words())
    for i, c in enumerate(brown_words):
        brown_words[i] = c.lower()

    lower = ' '.join(brown_words)
    brown = TextBlob(lower)
    for i, t in enumerate(brown.words):
        brown_words[i] = t.lemma
    lemma = ' '.join(brown_words)
    brown = TextBlob(lemma)

    text_freq = []
    brown_freq = []
    vocabulary = set(text.words)
    for v in vocabulary:
        if v in brown.words:
            text_freq.append(text.words.count(v))
            brown_freq.append(brown.words.count(v))
    print(np.array(text_freq), np.array(brown_freq))


if __name__ == '__main__':
    filename = ['DT.txt']
    for name in filename:
        with open(name, 'r+', encoding='utf-8') as f:
            text = f.read()

    analysis(text)