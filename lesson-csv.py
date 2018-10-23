import csv
with open ("jiaozi.csv","w") as csvfile:
    writer  = csv.writer(csvfile)
    writer.writerow(['x','y','z'])
    writer.writerows([[1,2,3],[4,5,6],[7,8,9]])
with open("jiaozi.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
# -*- coding:utf-8 -*-
# import random
# import csv
# with open ("作业.csv",wb) as mycsv:
#     writer = csv.writer(mycsv)