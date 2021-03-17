# 최소공배수
import sys


cycle = int(sys.stdin.readline())

for i in range(cycle):
    num_list = list(map(int, sys.stdin.readline().split()))
    a = max(num_list)
    b = min(num_list)
    A, B = a, b
    while b != 0:
        a = a % b
        a, b = b, a

    print(int(A*B/a))
