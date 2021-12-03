# https://www.acmicpc.net/problem/1743

from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i,j))
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    cnt = 1
    while q:
        x, y = q.popleft()
        for a, b in d:
            nx, ny = x+a, y+b
            if (0<=nx<N) and (0<=ny<M) and (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


N, M, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1

res = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = 0
            res.append(bfs(i,j))

print(max(res))
