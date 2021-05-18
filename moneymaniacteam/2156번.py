N = int(input())

drink = [0 for _ in range(N)]
dp = [0 for _ in range(N)]
for i in range(N):
    drink[i] = int(input())

dp[0] = drink[0]
if N > 1:
    dp[1] = drink[0] + drink[1]
    if N > 2:
        dp[2] = max(dp[1], dp[0] + drink[2], drink[1] + drink[2])

for i in range(3, N):
    dp[i] = max(dp[i-2] + drink[i], dp[i-3] + drink[i] + drink[i-1], dp[i-1])



print(dp[N-1])


