# https://programmers.co.kr/learn/courses/30/lessons/12903

# solution
def solution(s):
    answer = ''
    if len(s)%2 == 1:
        k = len(s)//2
        answer = s[k]
    else:
        k = len(s)//2
        answer = s[(k-1):(k+1)]
        
    return answer
