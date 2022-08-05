# https://programmers.co.kr/learn/courses/30/lessons/72410

# solution1
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    while new_id.count('..') > 0:
        new_id = new_id.replace('..', '.')
    new_id = re.sub('^[.]|[.]$', '', new_id)
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
  
# solution2
def solution(new_id):
  new_id = new_id.lower()
  ori = new_id
  for i in range(len(ori)):
    if (ori[i].isdigit() == True): continue
    elif (ori[i].isalpha() == False) & (ori[i] not in ['-','_','.']):
      new_id = new_id.replace(ori[i],"")

  while new_id.count('..') != 0:
    new_id = new_id.replace('..','.')

  if len(new_id) == 0:
    pass
  elif len(new_id) == 1 and new_id == '.':
    new_id = 'a'
  elif new_id[0] == '.' and new_id[-1] == '.':
    new_id = new_id[1:-1]
  elif new_id[0] == '.':
    new_id = new_id[1:]
  elif new_id[-1] == '.':
    new_id = new_id[:-1]

  if len(new_id) >= 16:
    new_id = new_id[:15]
    if new_id[0] == '.':
      new_id = new_id[1:]
    elif new_id[-1] == '.':
      new_id = new_id[:-1]
  elif len(new_id) == 0:
    new_id = 'aaa'
  elif len(new_id) <= 2:
    new_id += new_id[-1]*(3-len(new_id))

  return new_id

