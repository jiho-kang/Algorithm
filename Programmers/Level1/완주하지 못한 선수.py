# https://programmers.co.kr/learn/courses/30/lessons/42576

# my solution
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]

import collections

# better solution
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
