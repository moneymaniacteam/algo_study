#피보나치와 결국 동일 i일때 경우의 수는 i-1일 때 경우의 수에 1붙인거랑
#i-2일때 경우의 수에 00을 붙이는 것과 동일.

n = int(input())

result = []

result.append(1)
result.append(2)

for i in range(2, n):
    result.append((result[i-1] + result[i-2])%15746)

print(result[n-1])
