tmp = inp = int(input())
count = 0
while True:
    ten = tmp//10
    one = tmp % 10
    res = ten + one
    count += 1
    tmp = int(str(tmp % 10)+str(res % 10))

    if (inp == tmp):
        break

print(count)


# tmp = 1
# inp = 2

# cs = (tmp%10 + inp%10)
# print(type(cs))
