# 정수 삼각형
import sys


def input():
    return sys.stdin.readline().strip()


n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            a[i][0] = a[i-1][0] + a[i][0]
        elif i == j:
            a[i][j] = a[i-1][j-1] + a[i][j]
        else:
            a[i][j] = max(a[i-1][j-1] + a[i][j], a[i-1][j] + a[i][j])

print(max(a[n-1]))
