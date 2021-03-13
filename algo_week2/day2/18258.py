# 스택
import sys

input = sys.stdin.readline

stk = []


def f_push(str):
    stk.append(str)


def f_pop():
    if len(stk) == 0:
        print("-1")
    else:
        print(stk.pop())


def f_size():
    print(len(stk))


def f_empty():
    if len(stk) == 0:
        print("1")

    else:
        print("0")


def f_top():
    if len(stk) == 0:
        print("-1")

    else:
        print(stk[-1])


time = int(input())

for i in range(time):
    fuc = input().split()

    if fuc[0] == 'push':
        f_push(fuc[1])

    elif fuc[0] == 'pop':
        f_pop()

    elif fuc[0] == 'size':
        f_size()

    elif fuc[0] == 'empty':
        f_empty()

    elif fuc[0] == 'top':
        f_top()

#################################################################
