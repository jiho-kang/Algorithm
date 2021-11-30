# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

def dfs(v):
  print(v, end = ' ')
  visited_dfs[v] = True
  for idx, i in enumerate(graph[v]):
    if i == 1 and visited_dfs[idx] == False:
      dfs(idx)
    else:
      continue
    
def bfs(v):
  q = deque([])
  q.append(v)
  visited_bfs[v] = True
  print(v, end= ' ')

  while q:
    n = q.popleft()
    for idx, num in enumerate(graph[n]):
      if (visited_bfs[idx] == False) and (num == 1):
        q.append(idx)
        visited_bfs[idx] = True
        print(idx, end= ' ')

dfs(v)
print()
bfs(v)
