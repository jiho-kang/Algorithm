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


