input = [4, 6, 2, 9, 1]

# for i in range(5 - 1):
#     for j in range(5 - i):
#         print(i+j)


def selection_sort(array):
    n = len(array)  # O(n^2)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

            array[i], array[min_index] = array[min_index], array[i]
    # 이 부분을 채워보세요!
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
