# https://www.acmicpc.net/problem/2562

# 0 - 72ms / 77B
num = [int(input()) for i in range(9)]
print(max(num), num.index(max(num))+1)

# 1 - 68ms / 154B
answer = dict()
for i in range(1, 10):
    num = int(input())
    answer[num] = i
max_num = max(list(answer.keys()))
print(max_num)
print(answer[max_num])

# 2 - 72ms / 166B
answer = [-1,-1]
for i in range(1, 10):
    num = int(input())
    if answer[0] < num:
        answer[0] = num
        answer[1] = i
print(answer[0])
print(answer[1])
