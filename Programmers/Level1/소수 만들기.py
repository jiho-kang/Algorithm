# https://programmers.co.kr/learn/courses/30/lessons/12977

# solution1
def solution(nums):
    from itertools import combinations
    answer  = 0
    nums = combinations(nums,3)
    for num in nums:
        num = sum(num)
        for i in range(2, num+1):
            if num % i == 0:
                break
        if i == num:
            answer +=1
    return answer

# solution2
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
