# -*- coding:utf-8 -*-
import random
import string
def suijishengcheng(x,y):
    if type(x) != int or type(y) != int:
        return u"请输入数字"
    if x <= 0 or y <= 0:
        return u"请输入正数"
    L = (string.ascii_uppercase + string.digits)
    suijima = []
    while True:
        a=''.join(random.sample(L,x*4))
        b='-'.join(([a[i:i+4] for i in range(0,x*4,4)]))
        if b in suijima:  
            continue
        suijima.append(b) 
        if len(suijima) > y:
            break
    return suijima
print(suijishengcheng(4,10))

