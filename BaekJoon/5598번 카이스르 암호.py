# https://www.acmicpc.net/problem/5598
word = input()
answer = ''
for i in word:
    num = ord(i)
    if num > 67:
        answer += chr(num-3)
    else:
        answer += chr(num+23)
print(answer)
