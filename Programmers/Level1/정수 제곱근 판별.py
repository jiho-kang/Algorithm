#https://programmers.co.kr/learn/courses/30/lessons/12934#

# 내가 한 방법
def solution(n):
    answer = -1
    for i in range(1,n+1):
        if n // i == i and n%i == 0:
            answer = (i+1)**2
            break          
    return answer

# 똑똑해..
def solution(n):
    my = n**(1/2)
    answer = -1
    if my % 1 == 0:
        answer = (my+1)**2
    return answer
