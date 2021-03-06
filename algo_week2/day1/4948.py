# 베르트랑 공준


def isprime(m, n):
    count = 0
    n += 1                            # for문 사용을 위한 n += 1
    prime = [True] * n                # n개의 [True]가 있는 리스트 생성
    for i in range(2, int(n**0.5)+1):  # n의 제곱근까지만 검사  5
        if prime[i]:                    # prime[i]가 True일때
            for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
                prime[j] = False

    for i in range(m, n):
        if i > m and i < n:
            if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
                count += 1
    return count


while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(isprime(n, 2 * n))
###################################################
# import sys
# import math

# limit = 123456

# eratos = [1] * (2 * limit + 1)
# eratos[0] = 0
# eratos[1] = 0

# for i in range(2, int(math.sqrt(len(eratos)))):
#     if eratos[i]:
#         for j in range(i + i, len(eratos), i):
#             eratos[j] = 0

# while True:
#     n = int(sys.stdin.readline())

#     if n == 0:
#         break
#     else:
#     print(sum(eratos[n+1:(2*n)+1]))
