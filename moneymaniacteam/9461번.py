
T = int(input())
dp = [0 for _ in range(100)]


dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3,100):
    dp[i] = int(dp[i-2]) + int(dp[i-3])

for i in range(T):
    N = int(input())
    print(dp[N-1])
