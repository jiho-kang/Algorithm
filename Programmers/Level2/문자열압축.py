# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
  if len(s) == 1:
    return 1
  half = len(s)//2 +1
  # print(len(s), half)
  length_list = []

  for i in range(1, half):
    test = s[:i]
    result = ''
    cnt = 1
    # print(f"---------test word: <<{test}>> | s: <<{s}>>------")

    for j in range(i, len(s), i):
      if test == s[j:i+j]:
        cnt += 1
        # print(f"O: {test} == s[{j}:{i+j}]({s[j:i+j]})\n")
      else:
        if cnt == 1:
          cnt = ''
        # print(f"{test} != s[{j}:{i+j}]({s[j:i+j]})")
        result += str(cnt) +test
        test = s[j:i+j]
        cnt = 1
        # print(f'X: result는 {result}가 되었고, 이제부터 {test}가 있는지 검사합니다.\n')
    if cnt ==1:
      cnt = ''
    result += str(cnt) +test    
    # print(result)
    length_list.append(len(result))

  return min(length_list)
