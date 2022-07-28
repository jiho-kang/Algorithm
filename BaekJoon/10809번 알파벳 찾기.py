# https://www.acmicpc.net/problem/10809

# 72ms / 메모리:30840KB / 코드길이:151B
word = [x for x in input()]
for i in range(97, 123):
    try:
        print(word.index(chr(i)), end=' ')
    except:
        print(-1, end=' ')
       
