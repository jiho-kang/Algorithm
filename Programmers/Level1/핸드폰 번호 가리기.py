#https://programmers.co.kr/learn/courses/30/lessons/12948 
def solution(phone_number):
    length = len(phone_number[0:-4])
    value = ""
    value = ("*" * length) + (phone_number[-4:])


    return value
