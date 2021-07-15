#https://programmers.co.kr/learn/courses/30/lessons/12931

# my solution
def solution(n):
    numlist = list(map(int,str(n)))
    answer = 0
    for i in numlist:
        answer += i
    return answer

# considering time complexity
def sum_digit(number):
  if number < 10:
      return number;
  return (number % 10) + sum_digit(number // 10) 
