

import codes
'''
以下例子为创建一个类型结构Movie，然后将此类型通过codes模块保存到指定的文本文件，
然后从文本文件将保存的内容读出，文本文件的编码为UTF-8，文本的内容格式如下：
'''
def load_sentence(path):
    '''
    加载数据集，每一行至少包含一个汉字和一个标记
    句子与句子之间是以空格进行分割
    :param path:
    :return:
    '''
    # 存放数据集
    sentences= []
    # 临时存放每一个句子
    sentence = []

    for line in codes.open(path,'r',encoding='utf-8'):
        # 去掉两边的空格
        line = line.strip()
        if not line:
            if len(sentence) > 0:
                sentences.append(sentence)

