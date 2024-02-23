import jieba
import re


with open(r"D:\p3(2)\all_data.txt",'r',encoding='utf8') as fen:
    txt = set(fen.read().split('\t'))
with open("D:\p3(2)\hit_stopwords.txt",'r',encoding='utf8') as f:
    ting = f.read().split()
txt_lst = [word for word in jieba.lcut(''.join(txt)) if word not in ting]
for i in range(txt_lst.count('\n')):
    txt_lst.remove('\n')

print(txt_lst)
