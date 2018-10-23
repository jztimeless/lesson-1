# -*- coding: utf-8 -*-
import requests
import json
import csv

issuekey = 0
for issuekey
# 获取备注列
url  = 'http://www.tracup.com/apiv1/issue/getNoteList'
data = {        
        '_api_key':'6e238511179b6aeadf1e26fed1f6db07',
        'uKey':'414a471ef24654e6b8413416a5048238',
        'pKey':'f8da15073f3dad500a3ab4419a39304d',
        'iNo':'issuekey',
        'page':'1'
        }
beizhu = requests.post(url, data = data)
beizhu = beizhu.json()
print(beizhu)

all_items=beizhu['data']['list']
tittle=sorted(all_items[0].keys()) #获取所有列名


with open('tracup_beizhu.csv', 'w', newline='') as csvFile:
    # 标头在这里传入，作为第一行数据
    writer = csv.DictWriter(csvFile,tittle)
    writer.writeheader()       
    # 还可以写入多行
    writer.writerows(all_items)