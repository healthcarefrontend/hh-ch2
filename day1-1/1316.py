# 그룹 단어 체커

# a = int(input())
# count = 0

# for i in range(a):
#     str_input = input()  #happy
#     list_cha = []

#     for character in str_input:  # h a p p y
#         if len(list_cha) == 0:
#             list_cha.append(character)  # [h]

#         else:
#             if character not in list_cha:
#                 list_cha.append(character)   #[h, a, p]

#             else:  # list_cha에 있을 때
#                 if character != list_cha[-1]:  # 뒤에 다르면 break
#                     count += 1
#                     break

#                 elif character == list_cha[-1]:
#                     list_cha.append(character)


# print(a - count)
#########################################################################################################

N = int(input())

answer = 0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer += 1
print(answer)
