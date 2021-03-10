a, b = input().split()
clock = []

clock.append(int(a))
clock.append(int(b))

if clock[1] >= 45:
    clock[1] = clock[1] - 45
    print(clock[0], clock[1])

elif clock[1] < 45:
    if clock[0] > 0:
        clock[0] = clock[0] - 1
        clock[1] = clock[1] + 15

    elif clock[1] > 0:
        clock[0] = 23
        clock[1] = clock[1] + 15
print(clock[0], clock[1])
