h, m = map(int, input().split())

if m >= 45:
    m = m - 45

elif m < 45:
    if h == 0:
        h = 23
        m = m + 15

    else:
        h = h - 1
        m = m + 15

print(h, m)
