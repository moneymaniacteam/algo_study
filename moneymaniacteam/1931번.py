N = int(input())
meeting = [[0]*2 for _ in range(N)]
result =  [[0]*2 for _ in range(N)]
for i in range(N):
    start, end = map(int, input().split())
    meeting[i][0] = start
    meeting[i][1] = end

meeting.sort(key=lambda x: (x[1], x[0])) # 소트해주고 구해야됨

result[0][0] = meeting[0][0]
result[0][1] = meeting[0][1]
result_index = 0
for i in range(1,N):
    if meeting[i][0] <= result[result_index][0] and meeting[i][1] <= result[result_index][1]:
        result[result_index][0] = meeting[i][0]
        result[result_index][1] = meeting[i][1]

    if meeting[i][0] >= result[result_index][1]:
        result_index += 1
        result[result_index][0] = meeting[i][0]
        result[result_index][1] = meeting[i][1]


print(result_index+1)
