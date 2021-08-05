# https://programmers.co.kr/learn/courses/30/lessons/81301

# my solution
def solution(s):
    num = {'zero':0, 'one':1, 'two':2, 'three':3,
           'four':4, 'five':5, 'six':6, 'seven':7,
           'eight':8, 'nine':9}
    for eng in num.keys():
        if eng in s:
            s = s.replace(eng,str(num.get(eng)))
    return int(s)
