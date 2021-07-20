# https://programmers.co.kr/learn/courses/30/lessons/12918#

# my solutioin
def solution(s):
    number = "0123456789"
    answer = True
    for i in s:
        if (len(s) != 4and 6) or (i not in number):
            answer = False
    return answer
    
# better way
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
