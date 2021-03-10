num = int(input())
a = []
for i in range(num):
    [x, y] = map(int, input().split())
    rev = [y, x]
    a.append(rev)
b = sorted(a)
for i in range(num):
    print(b[i][1], b[i][0])


# N = int(input())
# a = [tuple(map(int, input().split())) for _ in range(N)]

# print(a)
# print(type(a[0]))
# print(type(a[0][1]))
# a = sorted(a, key=lambda x: x[0])
# a = sorted(a, key=lambda x: x[1])

# for i in a:
#     print(" ".join([str(_) for _ in i]))
