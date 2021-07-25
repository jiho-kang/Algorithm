# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

# my solution
def solution(n, arr1, arr2):
    import re
    adds = []
    for i in range(n):
      k = int(bin(arr1[i])[2:]) + int(bin(arr2[i])[2:])
      k = '0000' + str(k)
      k = k[-n:]
      adds.append(k)

    answer = []
    for j in adds:
      j = j.replace("0"," ")
      j = re.sub("[1-2]", "#", j)
      answer.append(j)

    return answer
    
# better solution
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
