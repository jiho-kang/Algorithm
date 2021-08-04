# https://programmers.co.kr/learn/courses/30/lessons/42748

# my solution
def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        c_n = commands[n]
        i = c_n[0]
        j = c_n[1]
        k = c_n[2]

        a2 = array[(i-1):j]
        a2.sort()
        add = a2[k-1]
        answer.append(add)
    return answer
