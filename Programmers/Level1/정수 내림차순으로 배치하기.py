#https://programmers.co.kr/learn/courses/30/lessons/12933

# my solution
def solution(n):
    my = list(str(n))
    my.sort(reverse=True)
    answer = ""
    for i in my:
        answer += str(i)
    return int(answer)
  
# considering time complex5
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
