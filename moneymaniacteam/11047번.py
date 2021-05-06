N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))

coin_num = 0

while K >0:
    money = coin[-1]
    for i in range(N):
        if K-coin[i]<0:
            money = coin[i-1]
            break
    temp = K//money
    coin_num += temp
    K -= temp*money


print(coin_num)