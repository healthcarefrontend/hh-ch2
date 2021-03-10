# 소수구하기

a, b = map(int, input().split())

prime_list = [2]

for n in range(a, b + 1):  # 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    for i in prime_list:
        if n % i == 0 and i * i <= n:
            break
    else:
        print(n)
        prime_list.append(n)
