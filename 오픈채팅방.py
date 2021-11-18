# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
  id_dict = dict()
  action_list = []
  ans = []
  for sentence in record:
    if len(sentence.split()) == 3:
      a, i, n = sentence.split()
      id_dict[i] = n
      action_list.append(a)
    else:
      a, i = sentence.split()
      action_list.append(a)

  # print('id_dict:', id_dict)
  # print('action_list:', action_list)

  for i, act in enumerate(action_list):
    id = record[i].split()[1]
    # print(f'{i}번째 id:{id}')
    # print('act:', act)
    if act == 'Enter':
      # print(id+id_dict[id])
      string = f'{id_dict[id]}님이 들어왔습니다.'
      # print(string)
      ans.append(string)
    elif act == 'Leave':
      string = f'{id_dict[id]}님이 나갔습니다.'
      ans.append(string)

  return ans
