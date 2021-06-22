import sys
f, m, i = map(int,sys.stdin.readline().split())
max = 0
if f>2*m :
    if f-(2*m) >= i:
        max = m
    else:
        k = f-i
        if k%3 == 0:
            max = m - (k // 3)
        else:
            max = m - (k // 3 ) - 1
else:
    if (f%2 > 0):
        f -= 1
        i -= 1

    if m-(f//2) > i:
        max = f//2
    else:
        k = i - (m - (f//2))
        if k % 3 == 0:
            max = m - (k//3)
        else:
            max = m - (k // 3 ) - 1

print(max)    