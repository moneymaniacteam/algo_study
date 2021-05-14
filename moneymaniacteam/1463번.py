N = int(input())

dp = [0 for _ in range(N+4)]

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:      # 2랑 3모두 나눠떨어지는경도 고려하기 위함.
        dp[i] = min(dp[i//3] + 1, dp[i])

print(dp)