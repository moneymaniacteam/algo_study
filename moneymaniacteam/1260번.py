
N, M, V = map(int, input().split())

line = [[0]*(N+1) for _ in range(N+1)]

def dfs(node):
    print(node, end = ' ')
    visit[node] = 1 #방문한 곳 1로 표시
    for i in range(N+1):
        if line[node][i] == 1 and visit[i] == 0:
            dfs(i)

def bfs(node):
    queue = []  #방문해야할 노드들 저장
    queue.append(node)
    visit[node] = 0 #방문한 곳 다시 0으로
    while queue != None:
        node = queue.pop(0)
        print(node, end =" ")
        for i in range(N+1):
            if visit[i] == 1 and line[node][i] == 1:
                queue.append(i)
                visit[i] = 0


for i in range(M):
    a, b = map(int, input().split())
    line[a][b] = line[b][a] = 1

visit = [0 for _ in range(N+1)]

dfs(V)
print("")
bfs(V)
