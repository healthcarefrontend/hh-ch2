# 이항계수
import sys


def factorial(a):
    num = 1
    for i in range(1, a + 1):
        num *= i

    return num


n, k = map(int, sys.stdin.readline().split())

print(int(factorial(n)/(factorial(k)*factorial(n-k))))
