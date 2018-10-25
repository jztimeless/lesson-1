#-*- coding:utf-8 -*-
with open('C:\Users\Joannd\Desktop\yisuoyuyan.txt','r') as f:
    s = f.read().strip()
    biaodianfuhao = [',','.','?','!',':',';','"',"'"]
    for i in biaodianfuhao:
        if i in s:
            s = s.replace(i,' ')
    list1 = s.split()
    rset1 = set(list1)
    
    dict1 = {}
    n = 0
    for word in rset1:
        if word in list1:      
            dict1[word] = list1.count(word)
    # print dict1
    print(sorted(dict1.items(), lambda x, y: cmp(x[1], y[1]), reverse = True))