# https://www.acmicpc.net/problem/1546

# 68ms / 메모리:30840KB / 코드길이:104B
cnt = int(input())
scores = list(map(int, input().split()))
m = max(scores)
print(sum(scores)/m*100/cnt)
