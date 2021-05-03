

n = int(input())

score = [0 for _ in range(301)]
result = [0 for _ in range(301)]

for i in range(1,n+1):
    score[i] = int(input())

result[1] = score[1]
result[2] = score[1]+ score[2]
result[3] = max(score[1]+score[3],score[2]+score[3])

for i in range(4,n+1):
    result[i] = max(result[i-3] + score[i-1] + score[i], result[i-2] + score[i])

print(result[n])



