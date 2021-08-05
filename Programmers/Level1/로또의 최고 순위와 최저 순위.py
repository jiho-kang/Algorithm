# https://programmers.co.kr/learn/courses/30/lessons/77484

# my solution
def solution(lottos, win_nums):
    count = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
        elif lottos[i] == 0:
            zero += 1
            
    lrank = 6
    if count >= 2:
        lrank = 7 - count
    
    hrank = 6
    count += zero
    if count+zero >= 2:
        hrank = 7-count
        
    return [hrank,lrank]
    

# shorter solution
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count +=1            
    
    return [rank[count+zero],rank[count]]
