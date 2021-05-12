N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000000
total = 0
for i in range(len(distance)):
    if i == 0:
        min_price = min(min_price, price[i])
        total += (distance[i] * min_price)
    else:
        min_price = min(min_price, price[i])
        total += (distance[i] * min_price)

print(total)