# https://www.acmicpc.net/problem/1037

# 72ms / 메모리: 20840KB / 코드길이: 79B
i = int(input())
num = list(map(int, input().split()))
print(min(num)*max(num))

# 72ms / 메모리: 20840KB / 코드길이: 162B
i = int(input())
num = list(map(int, input().split()))
num.sort()
if i % 2 ==0:
    answer = num[0] * num[-1]
else:
    answer = num[i//2]*num[i//2]
print(answer)
