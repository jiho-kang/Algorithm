# https://www.acmicpc.net/problem/2217

# solution
n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))
    #weight.append(int(sys.stdin.readline())) 를 넣는 것이 시간단축
weight.sort()

case = []
for i in range(n):
    case.append(weight[i]*(n-i))
    
print(max(case))

# my wrong solution
n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))
weight.sort()

while True:
  w = len(weight) * weight[0]
  if w < max(weight):
    del weight[0]
  else:
    print(w)
    break

    '''
w가 weight의 최댓값보다 클 경우라고 해도 무조건 답인 경우는 아니어서.
input이 n = 5 / 5, 8, 10, 16, 20로 주어질 경우를 생각해보면 첫번째 반복문에서 w=25이며 weight 최댓값인 20보다 크지만 두번째 반복문의 w=32가 될 수 있음.
'''
