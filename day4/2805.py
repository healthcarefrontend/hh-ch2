tree_num, need_length = map(int, input().split())

tree_list = list(map(int, input().split()))
##[20, 15, 10, 17]
guess_list = []
for i in range(1, max(tree_list)+1):
    guess_list.append(i)

current_min = 0  # 인덱스값
current_max = len(guess_list) - 1  # 인덱스값
current_guess = (current_min + current_max) // 2

while current_min <= current_max:

    if sum(tree_list)-(tree_num*guess_list[current_guess]) == need_length:
        print(guess_list[current_guess])

    elif sum(tree_list)-(tree_num*guess_list[current_guess]) > need_length:
        current_min = current_guess + 1
        print("wrong+1")

    else:
        current_max = current_guess - 1
        print("wrong-1")

    current_guess = (current_min + current_max) // 2


# print(tree_list)


# finding_target = 14
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_binary(target, array):
#     current_min = 0  # 인덱스값
#     current_max = len(array) - 1  # 인덱스값
#     current_guess = (current_min + current_max) // 2

#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True

#         elif array[current_guess] < target:
#             current_min = current_guess + 1

#         else:
#             current_max = current_guess - 1

#         current_guess = (current_min + current_max) // 2
#     return False


# result = is_existing_target_number_binary(finding_target, finding_numbers)
# print(result)
