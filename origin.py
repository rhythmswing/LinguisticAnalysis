import urllib.request
from lxml import etree
from io import StringIO
from textblob import TextBlob
import numpy as np

import time 
import sys

def get_origin(word):
    #url = 'http://www.etymonline.com/word/%s' % word
    url = 'https://en.wiktionary.org/wiki/%s' % word
    # print(url)
    html = urllib.request.urlopen(url)
    context = html.read().decode('utf-8')

# obtained from the website.
# origin_path = '//*[@id="root"]/div/div/div[3]/div/div/div[1]/div[2]/div/section/object/p[2]/text()[1]'
    #origin_path = '//*[@id="mw-content-text"]/div/p[3]/span[1]/span/a'
    origin_path = '//*[@id="mw-content-text"]/div/p[3]/span[1]/a'

    tree = etree.parse(StringIO(context), etree.HTMLParser())
    if len(tree.xpath(origin_path))>0:
        origin = tree.xpath(origin_path)[0].text
    else:
        origin = 'Not Found'
    return origin
    
def sample_origin(text, sample_size=100):
    words = TextBlob(text).words
    origins = []
    while len(origins) < sample_size:
        sys.stdout.write('\r%f%%' % (100.0 * len(origins) / sample_size))
        sys.stdout.flush()
        index = np.random.choice(len(words))
        if words[index].isalpha() and len(words[index]) > 1: 
            origin = get_origin(words[index].lower())
            if origin != 'Not Found':
                origins.append(origin)
        index+=1
    return origins

if __name__ == '__main__':
    files = ['speeches.txt', 'DT.txt', 'DT&HC.txt', 'DT&HC_T.txt', 'DT&HC_H.txt']
    for filename in files:
        print('Filename: ' + filename)
        with open(filename, 'r+', encoding='utf-8') as f:
            text = f.read()
            origins = sample_origin(text, 100)
            set_origins = set(origins)
            for o in set_origins:
                print('Percentage for %s: %f' % (o, 1.0 * origins.count(o) / len(origins)))
