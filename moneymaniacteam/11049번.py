N = int(input())
p = []


for i in range(N):
    row, col = map(int, input().split())
    if i == 0:
        p.append(row)
    p.append(col)

dp = [[0]*(N+1) for _ in range(N+1)]

for l in range(2, N+1):
    for i in range(1, N-l+2):
        j = i+l-1;
        dp[i][j] = (2 ** 32) -1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],  dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])


print(dp[1][N])
