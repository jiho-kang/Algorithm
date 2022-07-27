# https://www.acmicpc.net/problem/2444
# 1
n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print(' '*(n-i) + '*'*(2*i-1))
    else:
        num = 2*n - i
        print(' '*(i-n) + '*'*((2*num)-1))
        
# 2
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
