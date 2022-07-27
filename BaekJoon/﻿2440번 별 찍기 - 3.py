# https://www.acmicpc.net/problem/2440
# 1
n = int(input())
for i in range(n):
    print('*'*(n-i))
# 2 
n = int(input())
for i in range(n, 0, -1):
    print('*'*(i))
