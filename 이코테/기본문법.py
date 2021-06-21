####이코테 2021 강의

###사전자료형

#키와 값의 쌍을 데이터로 가지는 자료형 / 리스트와 튜플의 순차적 값 저장과 대비 됨
#변경 불가능한 자료형
A = dict()
A['키 값'] = 'value값'
A['사과'] = 'apple'
A['바나나'] = 'banana'
if '키 값' in A:
    print('키 값이라는 데이터가 존재합니다.')
    print("")
#키 데이터만 뽑고자 한다면
key_list = A.keys()
print('키 값만 :', list(key_list))
#값 데이터만 뽑고자 한다면
value_list = A.values()
print('값 데이터만 :',list(value_list))
#각 키에 따른 값을 하나씩 출력
print('각 키에 따른 데이터 값을 하나씩 출력')
for key in key_list:
    print(A[key])


###집합 자료형

#중복 허용 X, 순서 X so 데이터가 집합에 존재하는지 여부를 파악할 때 주로 사용
#데이터의 중복을 없앨 때 사용
#리스트 혹은 문자열을 초기ㅘ -> set()
#or 중괄호{} 안에 각 원소를 콤마를 기준으로 구분하여 삽입
#데이터 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있음

data_1 = set([1,1,2,3,3,4,5,5,0,0])
data_2 = {6,8,7,8,7,6,8,9,5}
print(data_1) #{0,1,2,3,4,5}
print(data_2) #{5,6,7,8,9}

#합집합, 교집합, 차집합 연산이 가능
#합집합 기호가 뭐지? : print(data_1:data_2)
print(data_1 & data_2) #{5}
print(data_1 - data_2) #{0, 1, 2, 3, 4}

#추가 및 제거
data_1.add(100) #{0,1,2,3,4,5,100}
data_1.update([55,66])  #{0,1,2,3,4,5,100,66,55}
data_1.remove(100)  #{0,1,2,3,4,5,66,55}


### 정리
#리스트, 튜플은 순서 0 -> 인덱싱으로 값 얻기 0
#사전자료형, 집합자료형은 순서 X -> 인덱싱으로 값 얻기 X
#사전의 키값 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회


### 기본 입출력
#input()
#map(): 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
#list(map(int, input().split())
#or a, b, c = map(int, input().split())
# EX) 학생 성적을 입력 받아 공백을 기준으로 구분하여 내림차순 정렬
score = list(map(int, input('학생 성적을 공백 기준으로 입력하세요 ').split()))
score.sort(reverse=True)
print(score)

#사용자로부터 빠르게 입력 받기
#sys.stdin.readline()메서드 사용
#rstrip() 입력 후 엔터가 줄 바꿈 기호로 입력되도록 하는 함수
import sys
print('숫자 하나 입력')
data = sys.stdin.readline().rstrip()
print(data)
#입력이 더이상 들어오지 않는다면? sys.stdin 사용
import sys
a,b = map(int, sys.stdin.readline().split())
print(a+b)

#줄바꿈 원하지 않을 때는 print(4, end=" ")

#f-string: 문자, 숫자를 간단히 함께 출력할 때 / 파이썬3.6부터 사용 가능
answer = 7
print(f"정답은 {answer}입니다.")