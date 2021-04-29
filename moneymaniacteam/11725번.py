import sys
sys.setrecursionlimit(200000)

n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [-1]*(n+1)         #각 노드의 부모 정보 담음
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)       #연관된 노드들 정보 입력
    tree[b].append(a)

def dfs(node):
    for i in tree[node]:
        if parent[i] == -1:
            parent[i] = node
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])