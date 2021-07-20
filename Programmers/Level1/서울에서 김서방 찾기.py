# https://programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    answer=[]
    for n in range(len(seoul)):
        if 'Kim' == seoul[n]:
            answer =('김서방은 {}에 있다'.format(n))
            return answer
