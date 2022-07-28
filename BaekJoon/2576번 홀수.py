# https://www.acmicpc.net/problem/2576

# 68ms / 메모리: 30840KB / 코드길이: 118B
num = [x for x in [int(input()) for _ in range(7)] if x%2 == 1]
print(-1 if len(num)<1 else f'{sum(num)}\n{min(num)}')

# 72ms / 메모리: 30840KB / 코드길이: 205B
num = []
check = True
for _ in range(7):
    i = int(input())
    if i%2 == 0:
        pass
    else:
        num.append(i)
        check = False
if check:
    print(-1)
else:
    print(sum(num), min(num))
