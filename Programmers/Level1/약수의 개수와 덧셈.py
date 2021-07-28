# https://programmers.co.kr/learn/courses/30/lessons/77884

# solution

def fx(n):
    list = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(i)
    return len(list)

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if fx(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
