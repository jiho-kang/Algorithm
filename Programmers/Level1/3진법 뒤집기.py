# https://programmers.co.kr/learn/courses/30/lessons/68935

# solution
def solution(n):
    answer = ""
    while n >= 1:
        k = n % 3 
        n //= 3
        answer = (str(k) + answer)
    result = 0
    
    answer = answer[::-1]
    result = int(answer,3)
    return 
    
    '''
    also can be below;
    
    for i in range(len(answer)):
      result += (3**i)*int(answer[i])
    '''
