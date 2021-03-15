# 파도반 수열
d = [0] * 101

d[0] = 0
d[1] = 1
d[2] = 1
d[3] = 1


def p(n):
    if n == 1 or n == 2 or n == 3:
        return 1

    if d[n] != 0:
        return d[n]

    d[n] = p(n-3) + p(n-2)
    return d[n]


cycle = int(input())

for i in range(cycle):
    num = int(input())
    print(p(num))
