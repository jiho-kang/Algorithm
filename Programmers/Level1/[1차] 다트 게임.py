# https://programmers.co.kr/learn/courses/30/lessons/17682#

# my solution
def solution(string):
  j = 0
  split = []
  for i in range(2,len(string)):
    if string[i-1:i+1] == "10":
      continue
    if string[i].isdigit() == True:
      split.append(string[j:i])
      j = i
    if len(split) == 2:
      split.append(string[j:])
      break
#   print(split)
  score = []
  for i in range(3):
    if "S" in split[i]:
      ind = split[i].find("S")
      num = int(split[i][:ind])
      score.append(num)
    elif "D" in split[i]:
      ind = split[i].find("D")
      num = int(split[i][:ind])
      score.append(num**2)
    elif "T" in split[i]:
      ind = split[i].find("T")
      num = int(split[i][:ind])
      score.append(num**3)
#     print('i here',score)

    if "*" in split[i]:
      if i == 0:
        score[i] = score[i] * 2
      else:
        score[i] = score[i] * 2
        score[i-1] = score[i-1] * 2
    elif "#" in split[i]:
      score[i] = score[i] * -1
#     print('i there',score)
  return sum(score)



# better solution
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
