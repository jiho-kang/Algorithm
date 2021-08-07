# https://programmers.co.kr/learn/courses/30/lessons/67256

# my solution
def solution(numbers,hand):
    import numpy as np
    
    m = {1:(0,3), 2:(1,3), 3:(2,3),
         4:(0,2), 5:(1,2), 6:(2,2),
         7:(0,1), 8:(1,1), 9:(2,1),
        '*':(0,0),0:(1,0),'#':(2,0),}
    
    LE = [1,4,7,'*']
    RI = [3,6,9,'#']
    L = '*'
    R = '#'
    answer = ''
    
    for n in numbers:
        L_dis = abs(m[n][0]-m[L][0]) + abs(m[n][1]-m[L][1])
        R_dis = abs(m[n][0]-m[R][0]) + abs(m[n][1]-m[R][1])
        if (n in LE):
            L = n
            answer += 'L'
        elif (n in RI):
            R = n
            answer += 'R'
        elif (L_dis < R_dis):
            L = n
            answer += 'L'
        elif (L_dis > R_dis):
            R = n
            answer += 'R'    
        elif L_dis == R_dis:
            if hand=='left':
                L = n
                answer += 'L'            
            if hand=='right':
                R = n
                answer += 'R' 
    return answer
