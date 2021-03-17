# # 다리놓기
# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = factorial(m) // (factorial(n) * factorial(m - n))
#     print(bridge)
##########################################################################
def combination(n, r):
    if dp[n][r] != 0:
        return dp[n][r]
    if r == 1:
        return n
    elif n == r:
        return 1
    else:
        dp[n][r] = combination(n-1, r) + combination(n-1, r-1)

    return dp[n][r]


if __name__ == "__main__":
    r, n = map(int, input().split())
    dp = [[0 for _ in range(r+1)] for _ in range(n+1)]
    ans = combination(n, r)
    print(ans)


dp = [[0 for _ in range(1 + 1)] for _ in range(5 + 1)]
print(dp)
