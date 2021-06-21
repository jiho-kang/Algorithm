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

# # 구현: 시뮬레이션과 완전 탐색

# ##### 구현: 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# ##### 완전탐색: 가능한 모든 경우의 수를 탐색하는 것
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
#     
#     알고리즘은 간단한데 코드가 지나칠 만큼 길어지거나,
#     실수 연산을 다루고, 특정 소수점 자리까지 출력
#     문자열을 특정한 기준에 따라 끊어 처리
#     적절한 라이브러리를 찾아서 사용해야 하는 문제 (순열, 조합)

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용됨
#
# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 사용됨

# ## 문제1
#     여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
#     가장 왼쪽 위에서 시작하며 좌표는 (1,1), 가장 오른쪽 아래 좌표는 (N,N)이다.
#     움직임은 상:U, 하:D, 좌:L, 우:R 로 이동할 수 있다.
#     이때 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
#     예를 들어 (1,)의 위치에서 L 혹은 U를 만나면 무시된다.
#     공간의 크기 N과 이동 계획이 주어질 때, 도착 지점의 좌표 (X,Y)를 공백을 기준으로 구분해서 출력하여라

# #### 내 문제

# +
n = int(input("N크기: "))
x, y = 1, 1
plans = input("plans: ").split()

#U, D, L, R 에 따른 움직임
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types = ["U","D","L","R"]

#이동 계획 하나씩 확인하기
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            if x+dx[i]<1 or y+dy[i]<1 or x+dx[i]>n or y+dy[i]>n:
                continue
            x += dx[i]
            y += dy[i]
        #공간을 벗어나는 경우에 무시하기

        #x,y = nx,ny

print(x,y)
        

# +
n = int(input("N크기: "))
x, y = 1, 1
plans = input("plans: ").split()

#U, D, L, R 에 따른 움직임
dx = [-1,1,0,0]
dy = [0,0,-1,1]
move_types = ["U","D","L","R"]

#이동 계획 하나씩 확인하기
for plan in plans:
    nx, ny = 0, 0
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        #공간을 벗어나는 경우에 무시하기
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx,ny

print(x,y)
# -

# ## 문제2
#     정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 
#     예를 들어 1을 입력?
#     ㄴ> 00시 00분 03초 / 00시 13분 03초

# #### 내 답

00분 00초에 들어갈 모든 경우의 수를 구하고
N=3,13 일 경우와 그렇지 않은 경우로 나누어서 구하기

# #### 해설

# +
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
print(count)
# -

# ## 문제3
# 체스판 8 x 8 좌표 평면이 있다. 나이트는 말을 타고 있기 때문에 이동할 때는 L자 형태로만 이동할 수 있으며, 정원 밖으로는 나갈 수 없다. 나이트 이동: 수평2 + 수직1 or 수직2 + 수평1.
#         
# 위치 좌표를 input, 이동할 수 있는 경우의 수는?
#    

# +
loca = input("위치: ")
x_index = loca[0]
letter = ['a','b','c','d','e','f','g','h']
x = letter.index(x_index) + 1
y = int(loca[1])

#우우위, 우우하, 좌좌위, 좌좌하, 우위위, 우하하, 좌위위, 좌하하
x_array=[-1,1,-1,1,-2,2,-2,2]
y_array=[2,2,-2,-2,1,1,-1,-1]

count = 0
for i in range(len(x_array)):
    nx, ny = 0, 0
    nx = x + x_array[i]
    ny = y + y_array[i]
    if nx<1 or ny<1 or nx>len(letter) or ny>len(letter):
        continue
    count +=1
print(count)
# -

# #### 해설

# +
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-1,2),(1,2),(-1,-2),(1,-2),(-2,1),(2,1),(-2,-1),(2,-1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >=1 and next_row<=8 and next_column>=1 and next_column <=8:
        count += 1
print(count)
# -

# ## 문제4
# 알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어진다. 모든 알파벳을 오름차숨으로 정렬하여 이어서 출력한 뒤에, 모든 숫자를 더한 값을 이어서 출력하라.

# +
data = input("문자열: ")
string_list = []
num = 0

for i in range(len(data)):
    if data[i].isnumeric():
        num += int(data[i])
    else:
        string_list.append(data[i])

string_list.sort()
if num>0: string_list.append(str(num))

#최종 결과 출력(리스트를 문자열로 변환하여 공백 없이 출력)
print(''.join(string_list))
# -


