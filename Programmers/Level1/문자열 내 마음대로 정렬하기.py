# https://programmers.co.kr/learn/courses/30/lessons/12915

# solution1
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        answer.append(strings[i][n]+strings[i])
    
    answer.sort()
    
    for j in range(len(answer)):
        answer[j] = answer[j][1:]  
        
    return answer
    
# solution2
def solution(strings, n):
    answer = sorted(sorted(strings), key = lambda x: x[n])
        
    return answer
