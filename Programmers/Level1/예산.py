# https://programmers.co.kr/learn/courses/30/lessons/12982

# solution
def solution(d,budget):
    d.sort()
    while sum(d) > budget:
        d = d[:-1]
    return len(d)
