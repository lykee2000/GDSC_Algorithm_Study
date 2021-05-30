# BOJ 11051 이항계수2

n, k = map(int, input().split())
dp = []

for i in range(n+1):
    dp.append([1]*(i+1))

for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]) % 10007  # nCr = n-1Cr + n-1Cr-1

print(dp[n][k])

# 더 짧은 버전
# from math import factorial
# n, k = map(int, input().split())
# result = factorial(n) // (factorial(k) * factorial(n - k))
# print(result % 10007)
