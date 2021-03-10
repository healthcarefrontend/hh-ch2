origin = input()  # 26
sub_origin = origin
other = -1
count = 0  # 숫자열이여야해

while other != origin:
    b = int(sub_origin[0]) + int(sub_origin[1])  # b = 8
    c = sub_origin[1] + str(b)  # c는 조합된 새로운 숫자 c =68
    other = c
    sub_origin = c
    count += 1

print(c)
