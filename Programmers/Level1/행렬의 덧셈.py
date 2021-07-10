#https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr1[0])
    for i in range(a):
        for j in range(b):
            arr1[i][j] = arr1[i][j] + arr2[i][j]

    
    return arr1
