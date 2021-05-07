
N = int(input())

card = list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

dp[1] = card[0]
dp[2] = max(card[0]*2, card[1])

for i in range(3, N+1):
    dp[i] = card[i-1]
    for j in range(1,i//2+1):
        dp[i] = max(dp[i], dp[i-j]+dp[j])

print(dp[N])