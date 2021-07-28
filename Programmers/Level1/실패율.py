# https://programmers.co.kr/learn/courses/30/lessons/42889

# solution
def solution(n, stages):
    stages.sort()
    dic = dict()
    result = []
    a = 0
    for i in range(1,n+1):
        if len(stages) - a > 0:
            b = stages.count(i) / (len(stages)-a)
            a += stages.count(i)
            dic[i]=b
        else:
            dic[i]=0
    return sorted(dic, key=lambda x : dic[x], reverse=True)
