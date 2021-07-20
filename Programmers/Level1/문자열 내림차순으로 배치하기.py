# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    a = list(s)
    a.sort(reverse=True)
    answer = ''.join(a)
    return answer
