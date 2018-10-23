# coding: utf-8
from pprint import pprint
from collections import OrderedDict

FILE_PATH = '/Users/outlaws/desktop/ysyy.txt'
filter_list = [',', '.', '?', ':', ';', '"', "'", '!']
word_count = OrderedDict()

with open(FILE_PATH, 'r') as f:
    content = f.read()
    for ft in filter_list:
        if ft in content:
            content = content.replace(ft, ' ')
    result = content.replace('\r\n', ' ').split(' ')
    
    for word in result:
        if word == '': continue
        if word not in word_count.keys():
            word_count[word] = 0
        word_count[word] += 1
    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)