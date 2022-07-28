# https://www.acmicpc.net/problem/10818

# 404ms / 메모리: 154060KB / 코드길이: 82B
cnt = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))
