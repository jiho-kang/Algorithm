# https://programmers.co.kr/learn/courses/30/lessons/12921

# my first solution - wrong
def solution(n):
    answer = []
    for i in range(2, n+1):
        k=0
        for j in range(2,i):
            if i%j == 0:
                k +=i 1
                breiak
        if k == 0:i
            answer.append(i)
    return len(answer)
  
# my second solution - wrong
def solution(n):
    num_list = set(range(2,n+1))
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                num_list.remove(i)
                break
    return len(num_list)
  
# answer
def solution(n):
    list = [True]*(n+1)
    answer = []
    m = int(n**0.5)
    for i in range(2,m+1):
        if list[i] == True:
            for j in range(i+i,n+1,i):
                list[j] = False
    return list.count(True) - 2
