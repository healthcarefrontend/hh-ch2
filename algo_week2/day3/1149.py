# # RGB 거리
# a = int(input())
# color_list = []
# color_list2 = [0] * (a + 1)


# def search_minimum(list):


# for i in range(a):
#     a, b, c = map(int, input().split())
#     color_list.append([a, b, c])


# print(color_list)


n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    print(i)
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
