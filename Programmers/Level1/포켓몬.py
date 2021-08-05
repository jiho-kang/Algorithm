# https://programmers.co.kr/learn/courses/30/lessons/1845

# my solution
def solution(nums):
  see = len(set(nums))
  n = int(len(nums)/2)
  if see > n:
    return n
  else:
    return see
    
# shortest solution
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
