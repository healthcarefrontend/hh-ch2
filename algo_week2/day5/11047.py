# # 동전 0
# import sys

# n, k = map(int, sys.stdin.readline().split())
# count = 0
# coin_list = []

# for i in range(n):
#     money = int(sys.stdin.readline())
#     coin_list.insert(0, money)

# while k != 0:
#     for coin in coin_list:  # [50000, 10000, 5000, 1000, 500, 100, 50, 10, 50, 5, 1]
#         count += k // coin
#         k = k % coin

# print(count)

#####################################################################
n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):  # 500000 10000 순으로 출력
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]
print(num)
