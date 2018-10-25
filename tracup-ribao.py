# -*- coding: utf-8 -*-
import requests
import json
import csv
import re
from pprint import pprint
import xlwt
from collections import Counter

#二维数组降一维函数
def flatten(a):
    for each in a:
        if not isinstance(each, list):
            yield each
        else:
            yield from flatten(each)

# 把固定的参数定义成变量, 因为参数会根据接口的不同而变化，但这些固定参数不会
u_key = '414a471ef24654e6b8413416a5048238'
api_key = '6e238511179b6aeadf1e26fed1f6db07'
p_key = '9df58763ae346255c4f3667bd8adf5bb'

#获取项目模块列表函数
def project_Module():
    url = 'http://www.tracup.com/apiv1/project/getProjectModuleList'
    data = {
        '_api_key': api_key,
        'uKey': u_key,
        'pKey': p_key
    }
    r = requests.post(url, data = data)
    # http请求可能会产生失败，需要判断失败
    if r.status_code == 200:
        r = r.json()
        return r['data']['list']
    raise Exception('接口请求失败')

#获取问题列表函数
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

#获取问题详情函数
def get_qestion(iNo):
    url  = 'http://www.tracup.com/apiv1/issue/view'
    data = {
        '_api_key': api_key,
        'uKey': u_key,
        'pKey': p_key,
        'iNo':iNo
        }
    r = requests.post(url, data = data)
    # http请求可能会产生失败，需要判断失败
    if r.status_code == 200:
        r = r.json()
        print(r)
        return r['data']
    raise Exception('接口请求失败')
    

# 获取项目所有状态函数
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

# 获取项目所有类型函数
def get_qestion_type():
    url  = 'http://www.tracup.com/apiv1/project/getProjectTypeList'
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


# 获得项目所有问题类型
# all_type = [i['projectTypeName']for i in get_qestion_type()['list']]
# print(all_type)
# 获得项目所有问题状态
# all_status = [i['list']['title']for i in get_qestion_status()]
# print(all_status)
#获得问题所有状态的key 
issueStatus = get_qestion_status()
status_key=[i['key'] for i in issueStatus]

all_issues = []
for s in status_key:
    result = get_qestion_list(s)
    if result is None:
        continue
    all_issues.append(result)


all_issues = list(flatten(all_issues))
# print(all_issues)

all_projet_module=project_Module()
project_module = []
for i in all_projet_module:
    moudle = i['projectModuleName']
    if moudle is None:
        continue
    project_module.append(moudle)
project_module=[i['projectModuleName'] for i in all_projet_module]
# print(project_module)

for i in project_module:
    issue = []
    module_issue={}
    issue_status=[]
    issue_type=[]
    
    # 取到各个模块下的问题列表
    for q in all_issues:
        if q['issueModule'] == i:
            issue.append(q['issueNo'])

    if len(issue) == 0:
        continue
    for issue_No in issue:
        question = get_qestion(issue_No)
        # pprint(question['info']['issueStatusText'])
        issue_status.append(question['info']['issueStatusText'])
        issue_type.append(question['info']['issueType'])
        
    #取到各模块问题列表
    module_issue[i] = issue  #组织：iNo
    #取到各模块问题状态
    module_issue['status']=issue_status
    module_issue['len_status'] = Counter(_status)
    # print(module_issue['len_status'])
    #取到各模块问题类型
    module_issue['type']=issue_type
    module_issue['len_type'] = Counter(issue_type)   
    # 取到各模块问题总数
    module_issue['len']=len(issue)
    # print(module_issue)

# file = workbook(encoding='utf-8')
# table = file.add_sheet('tracup_ribao')
# table_head = [['模块'],[issue_type],[status]]

# statistics = {}
# for q in all_issues:
#     # pprint(q)
#     key = '{}.{}.{}'.format(q['issueModule'], q['issueStatusText'], q['issueType'])
#     if key not in statistics.keys():
#         statistics[key] = []
#     statistics[key].append(q)
# # print(statistics)

# result = {}
# for key, group in statistics.items(): 
#     level1, level2, level3 = key.split('.')
#     result['moudle']=level1
#     result['status']=level2
#     result['type']=level3
#     # print(level1, level2, level3, len(group))
#     for i in project_module:
#         if level1 != i:
#             continue
#         module_status={}
#         status=[]
#         status.append(level2)
#         module_status[i]=status
#     print(module_status)


    