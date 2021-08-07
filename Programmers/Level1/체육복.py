# https://programmers.co.kr/learn/courses/30/lessons/42862

# my solution
def solution(n, lost, reserve):    
    slst = sorted(lost)
    srsv = sorted(reserve)
    print(slst,srsv)

    for k in reserve:
        if k in slst:
            slst.remove(k)
            srsv.remove(k)            
    
    for k in srsv:
        if (k-1) in slst:
            slst.remove(k-1)
        elif (k+1) in slst:
            slst.remove(k+1)

    return n - len(slst)
