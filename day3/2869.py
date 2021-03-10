import math

a, b, v = map(int, input().split())

print(math.ceil((v - b) / (a - b)))

# A, B, V = map(int, input().split())
# crawl = (V-B) / (A-B)
# print(int(crawl) + 1 if crawl % 1 > 0 else int(crawl))
