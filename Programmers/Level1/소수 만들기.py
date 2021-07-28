# https://programmers.co.kr/learn/courses/30/lessons/12977

# solution
def solution(nums):
    from itertools import combinations
    a = list(combinations(nums,3))
    b = []
    for i in range(len(a)):
        b.append(sum(a[i]))
        for j in range(2,sum(a[i])):
            if sum(a[i]) % j == 0:
                b.remove(sum(a[i]))
                break
    return len(b)
