# a, b = input()
# sum_i = 0
# cnt = 0

# while True:
#     for i in str(a):
#         sum_i += int(i)
#         print(sum_i)
#     a = ((int(a) % 10) * 10) + (sum_i % 10)
#     print(a)
#     cnt += 1

#     if a == int(b):
#         break

# print(cnt)

a, b = input()
sum_i = 0
cnt = 0

list_a = []
list_a.append(a)


for i in list_a:
    for num in str(i):
        print(num)
