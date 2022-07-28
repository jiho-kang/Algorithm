# https://www.acmicpc.net/problem/10872

# 72ms / 85B
num = int(input())
answer = 1
for i in range(2, num+1):
    answer *= i
print(answer)
