value = 1000- int(input())
sum = 0
coin = [500, 100, 50, 10, 5, 1]

for i in coin:
    sum += value // i
    value = value % i
print(sum)


