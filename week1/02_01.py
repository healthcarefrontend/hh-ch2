def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue ## 반복문의 다음 index로 넘어가게 함

        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] +=1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))