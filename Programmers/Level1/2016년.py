# https://programmers.co.kr/learn/courses/30/lessons/12901

# solution
def solution(a,b):
    import datetime as dt
    answer = dt.datetime(2016,a,b).weekday()
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = days[answer]
    return answer
