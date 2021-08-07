# https://programmers.co.kr/learn/courses/30/lessons/82612

# my solution
def solution(price, money, count):
    answer = -1
    need = 0
    for i in range(1,count+1):
        need += price*i
    if money >= need :
        return 0
    else:
        return need - money
