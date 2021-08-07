# https://programmers.co.kr/learn/courses/30/lessons/64061

# my solution
def solution(board, moves):
    import numpy as np
    moves = list(np.array(moves)-1)
    answer = 0
    ans = []

    for i in moves:
      for k in range(len(board)):
        if board[k][i] != 0:
          ans.append(board[k][i])
          board[k][i] = 0
          break
      if (len(ans)>1) and (ans[-1] == ans[-2]):
        answer += 2
        ans.pop(-1)
        ans.pop(-1)
    return answer
