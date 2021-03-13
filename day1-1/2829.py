# 설탕배달
inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break


# 설탕 배달
# def bag_count(weight):
#     bag_list = []
#     bag = 0
#     if (weight % 5) % 3 == 0:
#         bag = (weight // 5) + ((weight % 5) // 3)
#         bag_list.append(bag)

#     elif (weight % 3) % 5 == 0:
#         bag = (weight // 3) + ((weight % 3) // 5)
#         bag_list.append(bag)

#     elif weight % 5 == 0:
#         bag = weight // 5
#         bag_list.append(bag)

#     elif weight % 3 == 0:
#         bag = weight // 3
#         bag_list.append(bag)

#     else:
#         while True:
#             weight - 5


#     min_bag = min(bag_list)
#     return min_bag


# a = int(input())
# print(bag_count(a))
