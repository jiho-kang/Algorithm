# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&t=1630s
#

# ## 문제1
#     거스름돈 500, 100, 50, 10원 동전이 무한히 존재
#     거슬러줘야 할 돈이 N원일 때, 최소 동전의 개수

# #### 해설

# +
n = int(input("거스름 돈 (10의 배수여야 함): "))
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n//coin
    n %= coin
print(count)
# -

# ## 문제2
#     어떠한 수 N이 1이 될 때까지 [(1)N에서 1을 뺀다 (2)N을 K로 나눈다]를 반복적으로 선택하여 수행.
#     자연수 N과 K가 주어질 때, N이 1이 될 때까지 (1),(2)번을 수행하는 최소 횟수

# #### 내 답

# +
N = int(input("N: "))
K = int(input("K: "))
count = 0

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    count += 1
        
print(count)
# -

# #### 해설

# +
N, K = map(int, input().split())
count = 0

while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    count += 1
        
print(count)
# -

# ## 문제3
#     각 자리가 숫자 0부터 9로만 이루어진 문자열S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
#     숫자 사이에 X 혹은 + 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하라
#     모든 연산은 왼쪽부터 이루어짐

# #### 내 답

# +
n = input("수: ")
result = int(n[0])
for i in range(len(n)-1):
    if int(n[i+1]) <= 1 or result <=1:
        result += int(n[i+1])
    else:
        result *= int(n[i+1])
        
print(result)
# -

# #### 해설

# +
n = input()
result = int(n[0])

for i in range(1,len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
# -

# ## 문제4
#     모험가 N명의 '공포도'를 측정. 대처능력과 반비례
#     공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여
#     N명의 모험가의 공포도가 주어질 때, 최대 몇 개의 모험가 그룹을 만들 수 있는가? 여행을 떠날 수 있는 그룹 수의 최댓값

# #### 내 답

# +
n = input("모험가 수: ")
k = list(map(int,input("공포도: ").split()))
k.sort()

count = 0
while True:
    x = k[0]
    if x > len(k):
        break
    k = k[:x]
    count += 1 
print(count)
# -

# #### 해설

# +
n = input("모험가 수: ")
k = list(map(int,input("공포도: ").split()))
k.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수 

for i in k: #공포도가 낮은 것부터 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면
        result += 1 #그룹 결성
        count = 0 #현재 그룹 모험가 수 초기화
print(result)
# -
# https://covenant.tistory.com/131
#
# https://it-college-diary.tistory.com/entry/21-Greedy-Algorithm%ED%83%90%EC%9A%95%EB%B2%95-%EC%9A%95%EC%8B%AC%EC%9F%81%EC%9D%B4-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90

# ## 문제5 - 백준 11047 동전
# https://www.acmicpc.net/problem/11047
#
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
#
# #### 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
#
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
#
# #### 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
#
# #### 예제 입력
#     10 4200
#     1
#     5
#     10
#     50
#     100
#     500
#     1000
#     5000
#     10000
#     50000
#     
# #### 예제 출력
#     6


# ### 해설

# +
n, k = map(int,input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

count = 0
for i in coin:
    if k == 0:
        break
    count += k // coin
    k %= coin

print(count)
# -

# ## 문제6 - 백준 11399 ATM
# https://www.acmicpc.net/problem/11399
#
# 인하은행에는 ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.
#
# 사람들이 줄을 서는 순서에 따라서, 돈을 인출하는데 필요한 시간의 합이 달라지게 된다. 예를 들어, 총 5명이 있고, P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 인 경우를 생각해보자. [1, 2, 3, 4, 5] 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑을 수 있다. 2번 사람은 1번 사람이 돈을 뽑을 때 까지 기다려야 하기 때문에, 3+1 = 4분이 걸리게 된다. 3번 사람은 1번, 2번 사람이 돈을 뽑을 때까지 기다려야 하기 때문에, 총 3+1+4 = 8분이 필요하게 된다. 4번 사람은 3+1+4+3 = 11분, 5번 사람은 3+1+4+3+2 = 13분이 걸리게 된다. 이 경우에 각 사람이 돈을 인출하는데 필요한 시간의 합은 3+4+8+11+13 = 39분이 된다.
#
# 줄을 [2, 5, 1, 4, 3] 순서로 줄을 서면, 2번 사람은 1분만에, 5번 사람은 1+2 = 3분, 1번 사람은 1+2+3 = 6분, 4번 사람은 1+2+3+3 = 9분, 3번 사람은 1+2+3+3+4 = 13분이 걸리게 된다. 각 사람이 돈을 인출하는데 필요한 시간의 합은 1+3+6+9+13 = 32분이다. 이 방법보다 더 필요한 시간의 합을 최소로 만들 수는 없다.
#
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

# ### 내 답

# +
n = int(input())
time_list = list(map(int,input().split()))
#time_list = list(map(int,sys.stdin.readline().split()))
time_list.sort(reverse=True)

min = 0
for i in range(n):
    min += time_list[i] * (i+1)
print(min)
# -

# ## 문제7 - 백준 2217 로프
# https://www.acmicpc.net/problem/2217
#
# N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.
#
# 하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.
#
# 각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오. 모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

# +
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
# -

# ## 문제8 - 백준 2875 대회 or 인턴
# https://www.acmicpc.net/problem/2875
#
# 백준대학교에서는 대회에 나갈 때 2명의 여학생과 1명의 남학생이 팀을 결성해서 나가는 것이 원칙이다. (왜인지는 총장님께 여쭈어보는 것이 좋겠다.)
#
# 백준대학교는 뛰어난 인재들이 많아 올해에도 N명의 여학생과 M명의 남학생이 팀원을 찾고 있다. 대회에 참여하려는 학생들 중 K명은 반드시 인턴쉽 프로그램에 참여해야 한다. 인턴쉽에 참여하는 학생은 대회에 참여하지 못한다.
#
# 백준대학교에서는 뛰어난 인재들이 많기 때문에, 많은 팀을 만드는 것이 최선이다.
#
# 여러분은 여학생의 수 N, 남학생의 수 M, 인턴쉽에 참여해야하는 인원 K가 주어질 때 만들 수 있는 최대의 팀 수를 구하면 된다.


