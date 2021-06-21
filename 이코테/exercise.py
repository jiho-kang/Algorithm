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
            nx = x + dx[i]
            ny = y + dy[i]
        #공간을 벗어나는 경우에 무시하기
        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x,y = nx,ny

print(x,y)
