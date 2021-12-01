# https://www.acmicpc.net/problem/1303

n, m = map(int, input().split())
li = []
for i in range(m):
    li.append([k for k in input()])

def dfs_W(x,y):
    if (0<=x<m) and (0<=y<n):
        if li[x][y] == 'W':
            li[x][y] = 'W_'
            return 1 + dfs_W(x-1, y) + dfs_W(x+1, y) + dfs_W(x, y-1) + dfs_W(x, y+1)
        else:
            return False
    else:
        return False

def dfs_B(x,y):
    if (0<=x<m) and (0<=y<n):
        if li[x][y] == 'B':
            li[x][y] = 'B_'
            return 1 + dfs_B(x-1, y) + dfs_B(x+1, y) + dfs_B(x, y-1) + dfs_B(x, y+1)
        else:
            return False
    else:
        return False


ans = {'W':[], 'B':[]}
for i in range(m):
    for j in range(n):
        if li[i][j] == 'W':
            num = dfs_W(i,j)
            ans['W'].append(num * num)
        elif li[i][j] == 'B':
            num = dfs_B(i,j)
            ans['B'].append(num * num)
        else:
            continue

print(sum(ans['W']), sum(ans['B']))

