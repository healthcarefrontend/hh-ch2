# 최대공약수와 최소공배수

# 유클리드 호제법
import sys
A, B = map(int, sys.stdin.readline().split())
a, b = A, B

while b != 0:
    a = a % b
    a, b = b, a

# gcd
print(a)
# lcm
print(A*B//a)


# Mycode
# num1, num2 = map(int, input().split())
# num1_list = []
# num2_list = []
# same_list = []

# for i in range(1, num1+1):
#     if num1 % i == 0:
#         num1_list.append(i)

# for i in range(1, num2+1):
#     if num2 % i == 0:
#         num2_list.append(i)

# for i in num1_list:
#     for j in num2_list:
#         if i == j:
#             same_list.append(i)

# print(max(same_list))
# print(int((num1*num2)/max(same_list)))
