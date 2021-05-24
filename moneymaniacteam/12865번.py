N, K = map(int,input().split())

thing = [[0]*2 for _ in range(N+1)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    W, V = map(int, input().split())
    thing[i][0] = W
    thing[i][1] = V

for i in range(N+1):
    for j in range(1, K+1):
        if thing[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-thing[i][0]] + thing[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])