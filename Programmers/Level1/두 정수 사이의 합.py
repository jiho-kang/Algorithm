# https://programmers.co.kr/learn/courses/30/lessons/12912

# my solution
def solution(a, b):
    answer = 0
    a, b = min(a,b), max(a,b)
    for i in range(a,b+1):
        answer += i

    return answer
  
# better solution 1
def solution(a, b):
    mom = (abs(a-b)+1)/2
    answer = (a+b) * mom

    return answer
  
# better solution 2
def solution(a, b):
    a,b = min(a,b), max(a,b)

    return sum(range(a,b+1))
