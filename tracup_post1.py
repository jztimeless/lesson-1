# -*- coding: utf-8 -*-
import requests
import json
import csv

# 获取问题列表
url  = 'http://www.tracup.com/apiv1/issue/listIssue'
data = {
        '_api_key':'6e238511179b6aeadf1e26fed1f6db07',
        'uKey':'414a471ef24654e6b8413416a5048238',
        'pKey':'f8da15073f3dad500a3ab4419a39304d',
        'sortName':'i_no',
        'sort':'desc' 
        }
r = requests.post(url, data = data)
r = r.json()

all_issues=r['data']['list']
# print(all_issues) # all_issues是一个[]

issueNo = [] #项目全部问题的issuekey
i=0 #第几个问题
while i+1<=len(all_issues):
    issueNo.append(all_issues[i]['issueNo'])
    
# print(issueNo)

# 获取备注列
    url  = 'http://www.tracup.com/apiv1/issue/getNoteList'
    data = {        
            '_api_key':'6e238511179b6aeadf1e26fed1f6db07',
            'uKey':'414a471ef24654e6b8413416a5048238',
            'pKey':'f8da15073f3dad500a3ab4419a39304d',
            'iNo':all_issues[i]['issueNo'],
            'page':'1'
            }
    beizhu = requests.post(url, data = data)
    beizhu = beizhu.json()
    # print(beizhu)
    
    all_items=beizhu['data']['list']
    # print(all_items)
    
    issueNote=[]
    issueName=[]
    a=0
    while a+1<=len(all_items):
        issueNote.append(all_items[a]['issueNote'])
        a=a+1
    # print(issueNote)

    all_issues[i]['issueNote']=issueNote
    i=i+1
# print(all_issues)

tittle=sorted(all_issues[0].keys()) #获取所有列名


with open('tracup.csv', 'w', newline='') as csvFile:
    # 标头在这里传入，作为第一行数据
    writer = csv.DictWriter(csvFile,tittle)
    writer.writeheader()       
    # 还可以写入多行
    writer.writerows(all_issues)



