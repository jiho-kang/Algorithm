# https://programmers.co.kr/learn/courses/30/lessons/42840

# my solution
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    score = [0,0,0]

    for ind, ans in enumerate(answers):
      if ans == a[ind%5]: score[0] += 1
      if ans == b[ind%8]: score[1] += 1
      if ans == c[ind%10]: score[2] += 1

    result = []
    for person, sco in enumerate(score):
      if sco == max(score): result.append(person+1)
    return result
    
    
# similar solution
def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    ac=0
    bc=0
    cc=0
    for i in range(len(answers)):
      if a[i%5] == answers[i]:
        ac+=1
      if b[i%8] == answers[i]:
        bc+=1
      if c[i%10] == answers[i]:
        cc += 1
    
    answer = []
    k = max(ac,bc,cc)
    if k == ac: answer.append(1)
    if k == bc: answer.append(2)
    if k == cc: answer.append(3)
    
    return answer
