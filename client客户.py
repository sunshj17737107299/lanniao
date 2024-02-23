import requests
import json
from gensim.models import Word2Vec


def get_result(word1,word2):
    url = 'http://192.168.186.158:5000/nlp/made'
    model = Word2Vec.load(r"D:\p3(2)\wenben2\wenbenmoxing.bin")
    int_a = model.wv.similarity(word1,word2)
    data = {'res':str(int_a)}
    data_json = json.dumps(data)
    res = requests.post(url,data=data_json)
    print(res.json())


if __name__ == '__main__':
    get_result('西红柿','番茄')



# import requests
# import json
#
#
# def get_result(word):
#     url = 'http://192.168.186.158:5000/nlp/made'
#     data = {"word":word}
#     data_json = json.dumps(data) # 将字典转为JSON格式的字符串，因为request库在发送请求时需要字符串格式的数据
#     response = requests.post(url,data = data_json) # 发生POST请求
#     print(response.json()) # 打印相应内容，使用response.json()直接获取json格式的响应数据
#
#
# if __name__ == "__main__":
#     get_result('10')