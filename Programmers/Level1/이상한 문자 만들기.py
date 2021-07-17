# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    word_list = s.split(" ")
    answer_list=[]
    for word in word_list:
        answer_word =""
        for i in range(len(word)):
            if i % 2 == 1:
                answer_word += word[i].lower()
            else:
                answer_word += word[i].upper()
        answer_list.append(answer_word)
    return ' '.join(answer_list)
