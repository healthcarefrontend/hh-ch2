# 설탕 배달
def bag_count(weight):
    bag_list = []
    bag = 0
    if (weight % 5) % 3 == 0:
        bag = (weight // 5) + ((weight % 5) // 3)
        bag_list.append(bag)

    elif (weight % 3) % 5 == 0:
        bag = (weight // 3) + ((weight % 3) // 5)
        bag_list.append(bag)

    elif weight % 5 == 0:
        bag = weight // 5
        bag_list.append(bag)

    elif weight % 3 == 0:
        bag = weight // 3
        bag_list.append(bag)

    min_bag = min(bag_list)
    return min_bag


a = int(input())
print(bag_count(a))
