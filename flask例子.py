import json
from flask import jsonify
from flask import request
from flask import Flask
from gensim.models import Word2Vec


app = Flask(__name__)


def get_word(word):
    # model = Word2Vec(vector_size=100,window=5, min_count=5,workers=4)
    # model.build_vocab(corpus_file=r"D:\p3(2)\wenbenchuli\data.text")
    # to_word = sum(len(sentence.split()) for sentence in open("D:\\p3(2)\\wenbenchuli\\data.text", 'r', encoding='utf-8'))
    # model.train(corpus_file=r"D:\p3(2)\wenbenchuli\data.text",total_words=to_word,total_examples=model.corpus_count,epochs=5)
    # model.save('wenbenmoxing.bin')
    # model.wv.similarity('','')
    # # for w in model.wv.index_to_key:
    # #     print(w)
    # #     input()
    # return model.wv[word]
    return int(word)*int(word)

@app.route('/nlp/made',methods=['GET','POST'])
def nlp_service():
    data = request.get_data()
    result_data = json.loads(data)
    word = result_data.get('res','')
    # value = get_word(word)
    return jsonify({'code':200,'result':word})


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# print(get_word('10'))

# # 从flask框架中导入jsonify函数，用于将数据转换为JSON格式的响应
# from flask import jsonify
# # 从flask框架中导入request对象，用于获取客户端发送的请求数据
# from flask import request
# # 导入json模块，用于处理JSON数据
# import json
# # 从flask框架中导入Flask类，用于创建Web应用
# from flask import Flask
# # 创建一个Flask应用实例
#
#
# app = Flask(__name__)
# # 定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词
# def get_word(word):
#     return int(word)*int(word)
# # 使用app.route装饰器定义路由，指定URL路径和接受的请求方法
# @app.route("/nlp/made", methods=["GET", "POST"])
# # 定义处理该路由请求的函数
# def nlp_service():
#     # 从请求中获取数据
#     data = request.get_data()
#     # 将获取到的数据从JSON格式解析为Pyhton字典
#     result_data = json.loads(data)
#     # 从解析后的数据中获取键为”word“的值，如果不存在则默认为空字符串
#     word = result_data.get("word", "")
#     # 使用get_word函数处理获取到的单词
#     value = get_word(word)
#     # 使用jsonify函数构建JSON格式的响应，包含状态码和处理结果
#     return jsonify({"code": 200, "result": value})
# # 判断是否为主程序运行，而非模块导入
# if __name__ == "__main__":
#     # 启动Flask应用，指定监听的主机地址和端口号
#     app.run(host='0.0.0.0')