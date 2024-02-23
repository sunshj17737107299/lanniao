from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from itertools import chain
import jieba


def word_img(lst):
    word = WordCloud(font_path='SimHei.ttf')
    word_str = ' '.join(lst)
    word.generate(word_str)
    plt.figure()
    plt.imshow(word)
    plt.show()


lst = list(pd.read_csv('train.tsv',sep='\t')['sentence'])
with open("D:\p3(2)\hit_stopwords.txt",'r',encoding='utf8') as f:
    ting = f.read()
word_lst = list(chain(*map(lambda x:jieba.lcut(x),lst)))
for i in word_lst:
    if i in ting:
        word_lst.remove(i)
word_img(word_lst)
