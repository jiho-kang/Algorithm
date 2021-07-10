#https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    strx=str(x)
    k = 0
    for i in range(len(strx)):
        k += int(strx[i])
    if x % k == 0:
        return True
    else:
        return False
