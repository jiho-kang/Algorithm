# https://programmers.co.kr/learn/courses/30/lessons/12940

# 내가 푼 방법
def solution(n, m):
    answer = []
    small = 1
    # is_escape = False
    k = 0
    count = n if n < m else m
    while k <= count:       
        for i in range(2, n+1 if n < m else m+1):
            if n % i == 0 and m % i == 0:
                n //= i
                m //= i
                small *= i
                print('n:', n, 'm:', m, 'i:', i)
                break
            else:

                continue
        k += 1
    answer.append(small)
    print('small:',small)
    answer.append(small*n*m)
    print('small*n*m:',small*n*m)

    return answer

#유클리드 호제법
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
