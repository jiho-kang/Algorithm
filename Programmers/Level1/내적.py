# https://programmers.co.kr/learn/courses/30/lessons/70128

# my solution
def solution(a, b):
    import numpy as np
    answer = np.dot(a,b)
    return answer

# another solution
def solution(a,b):
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
