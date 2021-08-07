# https://www.acmicpc.net/submit/11047

# my solution
n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

lst.sort(reverse=True)

count = 0
for i in lst:
  if i <= k:
    count += k//i
    k %= i
    if k == 0:
      break
print(count)
