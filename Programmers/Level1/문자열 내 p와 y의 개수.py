# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    a = s.count('p') + s.count('P')
    print(a)
    b = s.count('y') + s.count('Y')
    print(b)
    if a == b:
        return True
    else:
        return False
