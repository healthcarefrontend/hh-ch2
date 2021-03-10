test_num = int(input())

for i in range(0, test_num):
    h, w, n = map(int, input().split())
    if n % h != 0:
        print((n % h) * 100 + (n // h + 1))

    else:
        print(h * 100 + (n // h))

# t = int(input())

# for i in range(t):  # range(2)  0 1
#     print(i)
#     print("hi")
#     h, w, n = map(int, input().split())

#     num = n // h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n // h
#         floor = h
#     print(f'{floor*100+num}')
