import jieba.posseg as jp
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from itertools import chain
import pandas


# -*- coding: utf-8 -*-


def get_xrc(text):
    data_lst = []
    for i in jp.lcut(text):
        if i.flag == 'a':
            data_lst.append(i.word)
    return data_lst


def get_word(word_lst):
    wordcloud = WordCloud(font_path='SimHei.ttf',max_words=100,background_color='black')
    word_key = ' '.join(word_lst)
    wordcloud.generate(word_key)
    plt.figure()
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()


train_data = pandas.read_csv('train.tsv',sep='\t')
test_data = pandas.read_csv('dev.tsv',sep='\t')
# train_voc = set(chain(*map(lambda x:jieba.lcut(x),train_data['sentence'])))
# print(len(train_voc))
# for i in map(lambda x:jieba.lcut(x),train_data['sentence']):
#     print(i)
# test_voc = set(chain(*map(lambda x:jieba.lcut(x),test_data['sentence'])))
# print(len(test_voc))
# print(len(list(chain(*map(lambda x:jieba.lcut(x),test_data['sentence'])))))

# label_1_train = train_data[train_data['label']==1]['sentence']
# label_0_train = train_data[train_data['label']==0]['sentence']
# train_lable_1 = chain(*map(lambda x:get_xrc(x),label_1_train))
# train_lable_0 = chain(*map(lambda x:get_xrc(x),label_0_train))
# get_word(train_lable_1)
# get_word(train_lable_0)
# label_1_test = test_data[test_data['label']==1]['sentence']
# label_0_test = test_data[test_data['label']==0]['sentence']
# test_lable_1 = chain(*map(lambda x:get_xrc(x),label_1_test))
# test_lable_0 = chain(*map(lambda x:get_xrc(x),label_0_test))
# get_word(test_lable_1)
# get_word(test_lable_0)


def create_set_num(lst,num):
    return set(zip(*[lst[i:] for i in range(num)]))


lst = [12,3,2,3,12,23,213,12,3,12,3,12,3]
num = 3
set = create_set_num(lst,num)
print(set)