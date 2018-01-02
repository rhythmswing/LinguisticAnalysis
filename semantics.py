from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


def analyze(text, filename='analysis'):
    corpus = TextBlob(text)

    sentences = corpus.sentences
    sentiments = {'polarity': [], 'subjectivity': []}

    for sent in sentences:
        sentiments['polarity'].append(sent.sentiment.polarity)
        sentiments['subjectivity'].append(sent.sentiment.subjectivity)

    for s in sentiments:
        sentiments[s] = np.array(sentiments[s])

    print(sentiments['polarity'].mean(), sentiments['polarity'].std())
    print(sentiments['subjectivity'].mean(), sentiments['subjectivity'].std())

    plt.figure(figsize=(9, 9))
    plt.xlabel('Polarity')
    plt.ylabel('Density')
    sn.distplot(sentiments['polarity'], bins=10)
    plt.savefig(filename + '_polarity.pdf')


sn.set(style='white', font_scale=3)


files = ['speeches.txt', 'DT.txt', 'DT&HC.txt',
         'DT&HC_T.txt', 'DT&HC_H.txt']
for filename in files:
    print('filename: ' + filename)
    with open(filename, 'r+', encoding='utf-8') as f:
        text = f.read()
    analyze(text, filename[:-4])
