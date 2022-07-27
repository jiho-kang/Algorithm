# https://www.acmicpc.net/problem/2441
# 1
n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i)+'*'*(i))

# 2
n = int(input())
for i in range(n):
    num = n-i
    print(' '*(n-num)+'*'*(num))
