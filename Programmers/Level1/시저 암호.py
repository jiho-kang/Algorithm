# https://programmers.co.kr/learn/courses/30/lessons/12926

import string
def solution(s, n):
    low = list(string.ascii_lowercase)
    high = list(string.ascii_uppercase)
    s = list(s)
    for i in range(len(s)):
        if s[i]==" ":
            continue
        elif s[i] in low:
            try:
              s[i] = low[low.index(s[i])+n]
            except IndexError:
              s[i] = low[low.index(s[i])+n-len(low)]
        else:
            try:
              s[i] = high[high.index(s[i])+n]
            except IndexError:
              s[i] = high[high.index(s[i])+n-len(high)]
    return ''.join(s)
