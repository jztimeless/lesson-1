# -*- coding: utf-8 -*-
import requests
import json
import csv
import re
from pprint import pprint
from collections import Iterable

#二维数组降一维函数
def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

# 把固定的参数定义成变量, 因为参数会根据接口的不同而变化，但这些固定参数不会
u_key = '414a471ef24654e6b8413416a5048238'
api_key = '6e238511179b6aeadf1e26fed1f6db07'
p_key = '9df58763ae346255c4f3667bd8adf5bb'

# 把单个接口封装成函数，方便调用
# 获取问题状态类型函数
def get_qestion_status():
    url  = 'http://www.tracup.com/apiv1/project/getStatusList'
    data = {
        '_api_key': api_key,
        'uKey': u_key,
        'pKey': p_key
    }
    r = requests.post(url, data = data)
    if r.status_code == 200:
        r = r.json()
        return r['data']['status']
    raise Exception('接口请求失败')   



# 获取问题列表函数
def get_qestion_list(status):
    url  = 'http://www.tracup.com/apiv1/issue/listIssue'
    data = {
        '_api_key': api_key,
        'uKey': u_key,
        'pKey': p_key,
        'sortName': 'i_no',
        'sort': 'desc' ,
        'status': status
    }
    r = requests.post(url, data = data)
    # http请求可能会产生失败，需要判断失败
    if r.status_code == 200:
        r = r.json()
        return r['data']['list']
    raise Exception('接口请求失败')

# 再定义一个获取备注的函数, issue_no从外部传进来
def get_issue_comment(issue_no):
    url  = 'http://www.tracup.com/apiv1/issue/getNoteList'
    data = {        
        '_api_key': api_key,
        'uKey': u_key,
        'pKey': p_key,
        'iNo': issue_no,
        # 'page': '1' # 这里按照一般的逻辑，如果传了页码参数，就只会给一页的数据
    }
    beizhu = requests.post(url, data = data)
    if beizhu.status_code == 200:
        r = beizhu.json()
        return r['data']['list']
    raise Exception('接口请求失败')

# 接下来定义一个函数用来过滤HTML标签
def filter_html(content):
    pat = re.compile('(?<=\>).*?(?=\<)')
    after_filter_contents = pat.findall(content)
    return ''.join(after_filter_contents)

#获得问题所有状态的key 
issueStatus = get_qestion_status()
status_key=[i['key'] for i in issueStatus]

all_issues=flatten([get_qestion_list(s) for s in status_key])

# all_issues=all_issues1[1]
print(all_issues)

issueNo = [] #项目全部问题的issuekey

# 现在开始遍历问题拿到备注
for q in all_issues:
    # 因为备注需要根据问题的issue_no获取，所以我们遍历可以拿到问题的issue_no再作为参数传给获取备注的函数，就能拿到每个问题的备注了
    comments = get_issue_comment(q['issueNo'])
    # 此时的comments变量应该是单个问题里的所有备注
    # 在把单个问题的所有备注集合在一起，作为一个大的字符串
    # 这里我做了判断，只有comments存在才走下面，这样会导致后面再导出的时候，有些有comment有些没有，造成报错
    # 先定义一个空值，把位置占住，后面当有的时候再覆盖掉
    q['issue_final_comment'] = ''
    if comments is None:
        continue
    issue_note_list = []
    
    for comment in comments:
        if comment is None:
            continue
        issue_note_list.append(comment['issueNote'])
    
    issue_all_comments = ' '.join(issue_note_list)
    # 这样就拿到了一个问题里面所有的备注，可以打印出来看看
    # 先要把HTML标签给去掉
    # 然后把这个备注，插入到q里面，在把q写入到csv，就可以导出了
    
    # 这就是过滤后的字符串
    final_comment = filter_html(issue_all_comments)
    
    # 然后我们把字符串写回到问题里面去
    q['issue_final_comment'] = final_comment
    
    
# 完成后把所有的问题打印出来看看
# 用带格式的打印 pprint = pretty print 是一中带格式的打印，看起来更好看
pprint(all_issues)

tittle=sorted(all_issues[0].keys()) #获取所有列名

with open('tracup.csv', 'w', newline='') as csvFile:
    # 标头在这里传入，作为第一行数据
    writer = csv.DictWriter(csvFile,tittle)
    writer.writeheader()       
    # 还可以写入多行
    writer.writerows(all_issues)












# 下面的是你的代码

# i=0 #第几个问题
# while i+1<=len(all_issues):
#     issueNo.append(all_issues[i]['issueNo'])
#     i=i+1
    
# print(issueNo)

# # 获取备注列
#     url  = 'http://www.tracup.com/apiv1/issue/getNoteList'
#     data = {        
#             '_api_key':'6e238511179b6aeadf1e26fed1f6db07',
#             'uKey':'414a471ef24654e6b8413416a5048238',
#             'pKey':'a6a5891ca82e0ff3b60a2c1fba3cfc98',
#             'iNo':all_issues[i]['issueNo'],
#             'page':'1'
#             }
#     beizhu = requests.post(url, data = data)
#     beizhu = beizhu.json()
#     print(beizhu)
#     i=i+1
    
#     all_items=beizhu['data']['list']
#     print(all_items)
    
# #     issueNote=[]
# #     a=0
# #     while a+1<=len(all_items):
# #         issueNote.append(all_items[a]['userName']+':'+all_items[a]['issueNote'])
# #         a=a+1
# #     # print(issueNote)

# #     all_issues[i]['issueNote']=issueNote
#     i=i+1
# # # print(all_issues)

# # tittle=sorted(all_issues[0].keys()) #获取所有列名


# with open('tracup.csv', 'w', newline='') as csvFile:
#     # 标头在这里传入，作为第一行数据
#     writer = csv.DictWriter(csvFile,tittle)
#     writer.writeheader()       
#     # 还可以写入多行
#     writer.writerows(all_issues)



