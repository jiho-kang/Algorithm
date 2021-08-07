# https://programmers.co.kr/learn/courses/30/lessons/76501

# my solution
def solution(absolutes, signs):
    answer = 0
    for num, see in zip(absolutes,signs):
        if see == True:
            answer += num
        else:
            answer -= num
    
    return answer
