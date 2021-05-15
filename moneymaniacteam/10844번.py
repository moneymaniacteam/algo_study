N = int(input())

dp = [[0]*(9) for _ in range(101)]


for i in range(9):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(9):
        if j == 8:
            dp[i][j] = dp[i - 1][j - 1]
        elif j == 0 and i > 2 :
            dp[i][j] = dp[i - 2][j] + dp[i - 1][j + 1]
        elif j == 0 and i == 2:
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]



print(sum(dp[N]) % 1000000000)




