# https://www.acmicpc.net/problem/2875

# solution
n, m, k = map(int, input().split())
count = 0
while n>=2 and m>=1 and n+m >= k+3:
  n -= 2
  m -= 1
  count += 1
print(count)


# my solution
a, b, k = map(int,input().split())

if a >= 2*b:
  g = b
  n = a - (2*b)
  while n < k:
    n += 3
    g -= 1
  print(g)

else:
  g = a//2
  n = (a - (2*g)) + (b - g)
  while n < k:
    n += 3
    g -= 1
  print(g)
