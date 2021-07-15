#https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) == 1:
        answer = [-1]
    else:
        arr.remove(min(arr))
        answer = arr
    return answer
