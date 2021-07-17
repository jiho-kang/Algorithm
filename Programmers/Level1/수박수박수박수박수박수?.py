# https://programmers.co.kr/learn/courses/30/lessons/12922

# my solution
def solution(n):
    answer = ''
    for i in range(n):
        if i %2 == 0:
            answer +='수'
        else:
            answer +='박'
    return answer
  
# smart solution...
def water_melon(n):
    s = "수박" * n
    return s[:n]
