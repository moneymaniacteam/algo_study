N = int(input())
M = int(input())

line = [[0]*(N+1) for _ in range(N+1)]

count = 0

def dfs(node):
    global count
    if node != 1:
        count += 1
    visit[node] = 1
    for i in range(N+1):
        if line[node][i] == 1 and visit[i] == 0:
            dfs(i)
    return int(count)
for i in range(M):
    a, b = map(int, input().split())
    line[a][b] = line[b][a] = 1

visit = [0 for _ in range(N+1)]

print(dfs(1))

