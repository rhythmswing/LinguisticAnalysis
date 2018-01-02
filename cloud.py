from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sn

files = ['speeches.txt', 'DT.txt', 'DT&HC.txt',
         'DT&HC_T.txt', 'DT&HC_H.txt']
for filename in files:
    with open(filename,'r+', encoding='utf-8') as f:
        text = f.read()

    wordcloud = WordCloud().generate(text)
    sn.set(style='white')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('cloud/'+filename[:-4]+'_cloud.pdf')
