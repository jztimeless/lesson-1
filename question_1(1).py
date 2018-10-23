# 题目：实现一个计算器，要求提供基本的 +，-，*，/ 功能
# 通过函数封装加减乘除操作，数据通过参数传入
# Python脚本要求能够接收外部的参数
# 如：执行 python question_1.py add 1 1 输出结果为2
# 执行 python question_1.py sub 2 1 输出结果为1
# 执行 python question_1.py multiply 2 3 输出结果为6
# 执行 python question_1.py divide 8 4 输出结果为2

# 要求输入非数字时，提示参数错误

import sys

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print '分母不能为0'
    return x / y

operator = sys.argv[1]
number1 = sys.argv[2]
number2 = sys.argv[3]

if operator.lower() not in ['add', 'sub', 'multiply', 'divide']:
    print '请输入正确的操作符'
    exit()

if not number1.isdigit() or not number2.isdigit():
    print '仅支持数字的计算'
    exit()

number1 = float(number1)
number2 = float(number2)

if operator == 'add':
    add(number1, number2)
elif operator == 'sub':
    sub(number1, number2)
elif operator == 'multiply':
    multiply(number1, number2)
elif operator == 'divide':
    divide(number1, number2)


