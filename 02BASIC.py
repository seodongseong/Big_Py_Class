
#------------------
# 리스트
#------------------
# 1. 리스트의 기본
'''
여러 값을 순서대로 저장할 수 있는 자료형
대괄호 [ ]로 정의
요소는 **인덱스(index)**로 접근 (0부터 시작)
'''
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])   # apple
# print(fruits[1])   # banana

# 2. 리스트 생성 방법
# 빈 리스트
# a = []
# b = list()
#
# # 초기값 포함
# nums = [1,2,3,4,5]
#
# # 다른 자료형도 혼합 가능
# mixed = [1, "hi", 3.14, True]

# 3. 주요 연산
'''
연산	설명	예시	결과
+	리스트 연결	[1,2] + [3,4]	[1,2,3,4]
*	리스트 반복	[0] * 3	[0,0,0]
in	포함 여부 확인	3 in [1,2,3]	True
len()	길이 확인	len([1,2,3])	3
'''


# 4. 요소 접근 / 슬라이싱
# nums = [10, 20, 30, 40, 50]
#
# print(nums[0])     # 10
# print(nums[-1])    # 50 (뒤에서 첫 번째)
# print(nums[1:4])   # [20, 30, 40]   (1~4-1)
# print(nums[0:-1])  # [10, 20, 30, 40]
# print(nums[:3])    # [10, 20, 30]   (0~3까지)
# print(nums[::2])   # [10, 30, 50] (2칸씩 건너뛰기)

# 5. 리스트 메서드
# fruits = ["apple", "banana", "cherry"]
#
# fruits.append("orange")   # 마지막에 추가 ['apple', 'banana', 'cherry', 'orange']
# print(fruits)
# fruits.insert(1, "grape") # 인덱스 1에 삽입   ['apple', 'grape', 'banana', 'cherry', 'orange']
# print(fruits)
# fruits.remove("banana")   # 특정 값 제거 ['apple', 'grape', 'cherry', 'orange']
# print(fruits)
# popped = fruits.pop()     # 마지막 요소 꺼내기  ['apple', 'grape', 'cherry']
# print(fruits)
# print("popped:", popped)  # popped: orange
# print(fruits)             # ['apple', 'grape', 'cherry']
#
# fruits.sort()             # 오름차순 정렬
# print(fruits)             # ['grape', 'cherry', 'apple']
# fruits.reverse()          # 반대로 뒤집기
# fruits.sort(reverse=True)
# print(fruits)             # ['grape', 'cherry', 'apple']
#
# count = fruits.count("apple")   # 개수 세기
# index = fruits.index("cherry")  # 위치 찾기

# 6. 리스트와 반복문
# nums = [1, 2, 3, 4, 5]
#
# # for문
# for n in nums:
#     print(n)
#
# # enumerate 사용
# for i, n in enumerate(nums):    #enum : 열거형 순서대로 번호를 지정해줌
#     print(i, n)

# 7. 리스트 컴프리헨션 (리스트를 간결하게 생성하는 문법)
# # 1~5 제곱수
# squares = [x**2 for x in range(1, 6)]
# print(squares)  # [1, 4, 9, 16, 25]
#
# # 짝수만 선택
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  # [0, 2, 4, 6, 8]

# 8. 2차원 리스트
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0])
#
# print(matrix[0][1])  # 2
# print(matrix[2][2])  # 9
#
# # 중첩 반복문으로 출력
# for row in matrix:
#     for val in row:
#         print(val, end=" ")
#     print()

# 9. 리스트 복사 주의
# a = [1, 2, 3]
# b = a          # 얕은 복사 (같은 객체) (주소 복사)
# c = a[:]       # 슬라이싱으로 복사 (새로운 객체)
# d = list(a)    # list()로 복사 (새로운 객체)
#
# a[0] = 100
# print("a:", a)  # [100, 2, 3]
# print("b:", b)  # [100, 2, 3] → 같은 객체라서 같이 변경됨
# print("c:", c)  # [1, 2, 3]
# print("d:", d)  # [1, 2, 3]

# 10. 리스트에 있는 문자열과 인덱스값 출력
# listbox = ['길벗','시나공','빅분기', '분석']
# for index, item in enumerate(listbox):
#     print(index, item)

'''
10. 정리
리스트는 가장 많이 쓰이는 시퀀스 자료형
다양한 자료형을 담을 수 있고, 동적으로 크기 변경 가능
슬라이싱, 반복문, 컴프리헨션 등 강력한 기능 제공
얕은 복사 vs 깊은 복사 구분 필요
'''

# 문제 1
'''
리스트 [10, 20, 30, 40, 50]에서
- 첫 번째 요소와 마지막 요소를 출력하시오.
'''
# li1 = [10,20,30,40,50]
# print(li1[0], li1[-1])


# 문제 2
'''
리스트 [1, 2, 3]에 4와 5를 추가한 뒤, 리스트를 출력하시오.
'''
# li2 = [1, 2, 3]
# li2.append(4)
# li2.append(5)
# print(li2)

# 문제 3
'''
리스트 [3, 6, 9, 12, 15]에서
- 인덱스 1~3 구간을 슬라이싱하여 출력하시오.
'''
# li3 = [3, 6, 9, 12, 15]
# print(li3[1:4])

# 문제 4
'''
리스트 [5, 2, 9, 1, 7]을 정렬하여 출력하고,
다시 반대로 뒤집어 출력하시오.
'''
# li4 = [5, 2, 9, 1, 7]
# li4.sort()
# li4.sort(reverse=True)
# print(li4)

# 문제 5
'''
1부터 5까지의 제곱수를 리스트 컴프리헨션으로 생성하고 출력하시오.
출력: [1, 4, 9, 16, 25]
'''
# li5 = [x**2 for x in range(1,6)]
# print(li5)





#------------------
# 딕셔너리
#------------------
# 1. 딕셔너리 기본
'''
키(key)와 값(value) 쌍을 저장하는 자료형
중괄호 {} 로 정의
키는 변경 불가능한 자료형(문자열, 숫자, 튜플 등)만 사용 가능
'''
# person = {"name": "Alice", "age": 25, "city": "Seoul"}
# print(person["name"])  # Alice

# 2. 딕셔너리 생성 방법
# 기본 생성
# d1 = {"a": 1, "b": 2}

# dict() 함수 활용
# d2 = dict(a=1, b=2)

# 리스트/튜플 쌍을 변환
# d3 = dict([("a", 1), ("b", 2)])

# print(d1, d2, d3)

# 3. 주요 연산
'''
연산	        설명	        예시      	        결과
len(d)	    항목 개수	len({"a":1,"b":2})	2
in	        키 존재 여부	"a" in d	        True
d[key]	    값 조회	    d["a"]	            1
d[key] = v	값 변경/추가	d["c"]=3	        {"a":1,"b":2,"c":3}
del d[key]	항목 삭제	del d["a"]	        {"b":2}
'''

# 4. 딕셔너리 메서드
# person = {"name": "Alice", "age": 25, "city": "Seoul"}
#
# # 키, 값, 쌍
# print(person.keys())     # dict_keys(['name', 'age', 'city'])
# print(person.values())   # dict_values(['Alice', 25, 'Seoul'])
# print(person.items())    # dict_items([('name','Alice'),('age',25),('city','Seoul')])
#
# # get() : 키 없을 때 None 반환
# print(person.get("age"))       # 25
# print(person.get("country"))   # None
# print(person.get("country", "없음"))  # 없음
#
# # pop() : 특정 키 제거 + 값 반환
# age = person.pop("age")
# print(age, person)
#
# # update() : 다른 딕셔너리 병합
# person.update({"job": "teacher"})
# print(person)


# 5. 반복문과 딕셔너리
'''
[in java]
public static void main(String [] args)
{
        Map<String, Object> map = new HashMap();
        map.put("k1","v1");
        map.put("k2","v2");
        map.put("k3","v3");
        map.put("k4","v4");
        
        for(String key : map.keySet());
}
'''
# scores = {"kim": 90, "lee": 85, "park": 95}
#
# # 키만 반복
# for k in scores:
#     print(k)
#
# # 값만 반복
# for v in scores.values():
#     print(v)
#
# # 키와 값 동시 반복
# for k, v in scores.items():
#     print(k, v)

# 6. 딕셔너리 컴프리헨션
# # 1~5까지 제곱 딕셔너리 만들기
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}
#
# # 조건 추가
# evens = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# print(evens)     # {2:4, 4:16}


# 7. 중첩 딕셔너리
# students = {
#     "kim": {"age": 20, "major": "CS"},
#     "lee": {"age": 22, "major": "Math"}
# }
# print(students["kim"])  # {'age': 20, 'major': 'CS'}
# print(students["lee"])  # {'age': 22, 'major': 'Math'}
# print(students["kim"]["major"])  # CS
# s = {
#     "k1": ["v1-1","v1-2","v1-3"],
#     "k2": ["v2-1","v2-2","v2-3"],
#     "k3": ["v3-1","v3-2","v3-3"]
# }
# print(s["k1"])  #['v1-1', 'v1-2', 'v1-3']
# print(s["k1"][0])  #v1-1
# print(s["k1"][-1])  #v1-3

# 8. 딕셔너리 반복문
# person_info = {
#     'name': '사랑',
#     'age': 20,
#     'city': '부산',
#     'hobbies': ['연애', '수영', '코딩']
# }
# for k, v in zip(person_info.keys(), person_info.values()):
#     print(k, v)
#
# for k, v in person_info.items():
#     print(k, v)

# name 사랑
# age 20
# city 부산
# hobbies ['연애', '수영', '코딩']

# 9. 정리
'''
딕셔너리는 Key-Value 구조로 데이터 관리에 적합
keys(), values(), items() 메서드 자주 활용
get()으로 안전한 조회 가능
컴프리헨션으로 간결하게 생성 가능
중첩 구조를 이용해 JSON 형식 데이터 처리 가능
'''
# 미니 실습 문제
# 문제 1
'''
딕셔너리 {"name":"kim", "age":20, "city":"Seoul"}에서
- name과 city를 출력하시오.
'''
# di1 = {"name":"kim", "age":20, "city":"Seoul"}
# print(di1["name"],di1["city"])

# 문제 2
'''
빈 딕셔너리를 만든 후,
- "math"=90, "eng"=85 를 추가하고 전체를 출력하시오.
'''
# di2 = {}
# di2["math"]=90
# di2["eng"]=85
# print(di2)

# 문제 3
'''
딕셔너리 {"a":1, "b":2, "c":3}에서
- 키만 출력하고
- 값만 출력하고
- 키와 값을 함께 출력하시오.
'''
# di4 = {"a":1, "b":2, "c":3}
# print(di4.keys(), di4.values(),di4.items())


# 문제 4
'''
딕셔너리 {"apple":1000, "banana":2000, "cherry":3000}에서
- "banana"의 값을 2500으로 수정하고
- "orange"=1500을 추가한 뒤
전체를 출력하시오.
'''
# di5 = {"apple":1000, "banana":2000, "cherry":3000}
# di5["banana"] = 2500
# di5["orange"] = 1500
# print(di5)

# 문제 5
'''
딕셔너리 컴프리헨션으로
1~5까지 숫자를 키로 하고, 제곱을 값으로 하는 딕셔너리를 생성하시오.
'''
# di6 = {x: x**2 for x in range(1, 6)}
# print(di6)

#------------------
# 튜플
#------------------
# 1. 튜플 기본
'''
리스트와 비슷하지만 수정 불가능(immutable) 한 자료형
소괄호 ( )로 정의
인덱스로 접근 가능
'''
# t = (10, 20, 30)
# print(t[0])   # 10
# print(t[-1])  # 30

# 2. 튜플 생성 방법
# # 기본 생성
# a = (1, 2, 3)
#
# # 소괄호 생략 가능
# b = 4, 5, 6
#
# # 요소가 하나일 때는 반드시 콤마 필요
# c = (7,)
# d = 7,
#
# # 빈 튜플
# empty = ()
# print(a, b, c, d, empty)
#
# e = 7
#
# print(type(d))  # <class 'tuple'>
# print(type(e))  # <class 'int'>

# 3. 튜플과 리스트 차이
'''
리스트: 변경 가능(mutable) → 추가, 삭제, 수정 가능
튜플: 변경 불가능(immutable) → 읽기 전용 데이터에 적합
'''
# lst = [1, 2, 3]
# tpl = (1, 2, 3)
#
# lst[0] = 100    # 가능
# # tpl[0] = 100  # 오류 (TypeError)


# 4. 주요 연산
'''
연산	    설명	        예시	                결과
+	    연결	        (1,2)+(3,4)	        (1,2,3,4)
*	    반복	        (1,2)*3	            (1,2,1,2,1,2)
in	    포함 여부	3 in (1,2,3)	    True
len()	길이 확인	len((1,2,3))	    3
슬라이싱	부분 추출	(10,20,30,40)[1:3]	(20,30)
'''

# 5. 패킹(Packing)과 언패킹(Unpacking)
# # 패킹: 여러 값을 하나의 튜플로 묶음
# t = 1, 2, 3
#
# # 언패킹: 튜플을 여러 변수에 나눠 담음
# a, b, c = t
# print(a, b, c)   # 1 2 3
#
# # *을 이용한 언패킹
# nums = (1, 2, 3, 4, 5)
# x, y, *rest = nums
# print(x, y, rest)  # 1 2 [3,4,5]


# 6. 튜플과 함수 반환값 (함수는 여러 값을 튜플로 반환할 수 있음)
# def calc(a, b):
#     return a+b, a*b
#
# result = calc(3, 4)
# print(result)        # (7, 12)
#
# s, m = calc(3, 4)    # 언패킹
# print(s, m)          # 7 12
#
# # 7. 튜플 활용
# '''
# 데이터 변경을 막아 안전하게 사용 가능
# 딕셔너리의 키, 집합의 원소로 사용 가능 (리스트는 불가능)
# '''
# d = {(1,2): "point A", (3,4): "point B"}
# print(d[(1,2)])   # point A

# 8. 정리
'''
튜플은 변경 불가능한 시퀀스 자료형
리스트보다 메모리 효율이 좋음
패킹/언패킹에 유용
함수에서 여러 값을 반환할 때 많이 사용
'''

# 미니 실습 문제
# 문제 1
'''
튜플 (10, 20, 30, 40, 50)에서
- 첫 번째 값과 세 번째 값을 출력하시오.
'''
# t1 = (10, 20, 30, 40, 50)
# print(t1[0], t1[2])
# 문제 2
'''
튜플 (1, 2, 3)과 (4, 5)를 이어 붙여 출력하시오.
'''
# t2 = (1,2,3)
# t3 = (4,5)
# t4 = t2 + t3
# print(t4)

# 문제 3
'''
튜플 (100, 200, 300, 400, 500)에서
- 인덱스 1~3 범위를 슬라이싱하여 출력하시오.
'''
# t5 = (100, 200, 300, 400, 500)
# print(t5[1:4])

# 문제 4
'''
튜플 (1, 2, 3)을 언패킹하여
변수 a, b, c에 저장한 뒤 출력하시오.
'''
# t6 = (1,2,3)
# a,b,c = t6
# print(a,b,c)
# 문제 5
'''
함수 calc(x, y)를 만들어
x+y와 x*y를 튜플로 반환하고,
그 결과를 언패킹하여 출력하시오.
'''
# def calc(x,y):
#     return x+y, x*y
# result = calc(3, 4)
# print(result)        # (7, 12)
#
# s, m = calc(3, 4)    # 언패킹
# print(s, m)          # 7 12



#------------------
# 인덱싱/슬라이싱
#------------------
# 1. 인덱싱 (Indexing)
'''
시퀀스 자료형(문자열, 리스트, 튜플 등)에서 특정 위치의 요소를 가져오는 방법
0부터 시작하는 정수 인덱스를 사용
음수 인덱스는 뒤에서부터 접근
'''
# data = ["a", "b", "c", "d", "e"]
#
# print(data[0])   # 첫 번째 요소 → a
# print(data[2])   # 세 번째 요소 → c
# print(data[-1])  # 마지막 요소 → e
# print(data[-2])  # 뒤에서 두 번째 → d

# 2. 슬라이싱 (Slicing)
'''
시퀀스 자료형에서 범위 지정으로 일부를 추출
[start:end:step] 형식
start: 시작 인덱스 (포함)
end: 끝 인덱스 (포함X)
step: 간격 (기본값 1)
'''
# nums = [10, 20, 30, 40, 50]
#
# print(nums[1:4])    # 인덱스 1~3 → [20, 30, 40]
# print(nums[:3])     # 처음부터 인덱스 2까지 → [10, 20, 30]
# print(nums[2:])     # 인덱스 2부터 끝까지 → [30, 40, 50]
# print(nums[::2])    # 처음부터 끝까지, 2칸씩 → [10, 30, 50]
# print(nums[::-1])   # 거꾸로 뒤집기 → [50, 40, 30, 20, 10]

# 3. 문자열에서 인덱싱/슬라이싱 (문자열도 시퀀스 자료형이므로 동일하게 사용 가능)
# text = "Python"
#
# print(text[0])     # P
# print(text[-1])    # n
# print(text[1:4])   # yth
# print(text[::-1])  # nohtyP


# 4. 튜플에서 인덱싱/슬라이싱 (튜플도 시퀀스이므로 동일하게 적용 가능)
# t = (100, 200, 300, 400)
#
# print(t[0])      # 100
# print(t[1:3])    # (200, 300)
# print(t[::-1])   # (400, 300, 200, 100)

# 5. 중첩 구조에서 인덱싱
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[0][1])   # 첫 번째 행, 두 번째 값 → 2
# print(matrix[2][2])   # 세 번째 행, 세 번째 값 → 9

# 6. 정리
'''
인덱싱: 특정 위치의 단일 값 추출
슬라이싱: 구간 단위로 값 추출 (시작 포함, 끝 제외)
step 활용으로 건너뛰기/역순 가능
문자열, 리스트, 튜플 등 모든 시퀀스 자료형에 적용 가능
'''
# 미니 실습 문제
# 문제 1
'''
리스트 ["a","b","c","d","e"]에서
- 첫 번째 값과 마지막 값을 출력하시오.
'''
# li1 = ["a","b","c","d","e"]
# print(li1[0],li1[-1])

# 문제 2
'''
리스트 [10, 20, 30, 40, 50]에서
- 인덱스 1~3 범위를 슬라이싱하여 출력하시오.
'''
# li2 = [10, 20, 30, 40, 50]
# print(li2[1:4])
# 문제 3
'''
문자열 "Python"에서
- 첫 글자와 마지막 글자를 출력하시오.
'''
# str1 = "Python"
# print(str1[0],str1[-1])

# 문제 4
'''
튜플 (100, 200, 300, 400, 500)에서
- 2칸씩 건너뛰어 출력하시오.
'''
# t1 = (100, 200, 300, 400, 500)
# print(t1[0:6:2])
# 문제 5
'''
리스트 [1,2,3,4,5]를
- 슬라이싱을 사용하여 거꾸로 출력하시오.
'''
# li3 = [1,2,3,4,5]
# li3.sort(reverse=True)
# print(li3)


#------------------
# 내장함수
#------------------
# 1. 합계 — sum()
'''
시퀀스(리스트, 튜플 등) 요소의 합을 구함
True는 1, False는 0으로 계산됨
'''
# listbox = [4, 2, 10, 6, 8]
# print(sum(listbox))   # 30
#
# boolbox = [True, False, True]
# print(sum(boolbox))   # 2

# 2. 최대값 — max() (시퀀스에서 가장 큰 값을 반환)
# listbox = [4, 2, 10, 6, 8]
# print(max(listbox))   # 10

# 3. 최소값 — min()   (시퀀스에서 가장 작은 값을 반환)
# listbox = [4, 2, 10, 6, 8]
# print(min(listbox))   # 2


# 4. 길이(갯수) — len()     (시퀀스 요소의 개수를 반환)
# listbox = [4, 2, 10, 6, 8]
# print(len(listbox))   # 5

# 5. 반올림 — round()
'''
지정한 소수점 자리까지 반올림
round(값, 소수점자리수)
'''
# print(round(1.2345, 2))   # 1.23
# print(round(1.2375, 2))   # 1.24

# 6. 정리
'''
sum() : 합계
max() / min() : 최대/최소
len() : 길이
round() : 반올림
→ 데이터 연산에서 가장 자주 사용하는 내장 함수들
'''
# 미니 실습 문제
# 문제 1
'''
리스트 [3, 7, 1, 9, 5]의 합계를 구하시오.
'''
# li1 = [3, 7, 1, 9, 5]
# print(sum(li1))

# 문제 2
'''
리스트 [12, 45, 7, 23, 89]에서 최대값과 최소값을 각각 구하시오.
'''
# li2 = [12, 45, 7, 23, 89]
# print("최댓값 : ", max(li2))
# print("최솟값 : ", min(li2))

# 문제 3
'''
문자열 "Hello Python"의 길이를 구하시오.
'''
# text = "Hello Python"
# print("문자열 길이 : ",len(text))

# 문제 4
'''
실수 3.14159를 소수점 둘째 자리까지 반올림하시오.
'''
# num = 3.14159
# print("소수점 둘째 자리까지 반올림 : ", round(num, 2))

# 문제 5
'''
리스트 [True, False, True, True]를 sum()으로 계산한 결과를 구하시오.
'''
# li3 = [True, False, True, True]
# print(sum(li3))



#------------------
# 문자열
#------------------
# 1. 문자열 변경 (replace)
'''
문자열 일부를 다른 문자열로 교체
문자열.replace("기존문자","새문자")
'''
# 한 단어 변경
# text = "빅데이터 분석기사 파이썬 공부"
# text = text.replace("공부", "스터디")
# print(text)
# '빅데이터 분석기사 파이썬 스터디'

# 여러 단어 변경 (연속 적용)
# text = "빅데이터 분석기사 파이썬 공부"
# text = text.replace("파이썬", "머신러닝").replace("분석기사", "분석을 위한")
# print(text)
# '빅데이터 분석을 위한 머신러닝 공부'

# 2. 문자열 슬라이싱
'''
문자열은 리스트처럼 인덱스로 접근 가능
[start:end] → start 포함, end 미포함
'''
# text = "안녕하세요! 함께 성장해요."
#
# print(text[:2])    # '안녕' (처음부터 2글자)
# print(text[7:9])   # '함께' (인덱스 7~8)
# print(text[-3:])   # '해요.' (뒤에서 3번째부터 끝까지)
# print(text[::-1])  # 역순 출력 '요해 장성 게함 !요세하녕안'

# 3. 문자열 분리 (split)
'''
특정 구분자로 나눠서 리스트로 반환
split("구분자"), 기본은 공백
'''
# date = "2022-12-25"
#
# print(date.split('-'))
# # ['2022', '12', '25']
#
# text = "안녕하세요! 함께 성장해요."
# print(text.split())
# # ['안녕하세요!', '함께', '성장해요.']

# 4. 문자열 → 리스트 변환
'''
list(문자열) : 문자열을 문자 하나하나로 분리
'''
# date = "2022-12-25"
# print(list(date))
# ['2', '0', '2', '2', '-', '1', '2', '-', '2', '5']

# 5. 문자열 결합 (join)
'''
리스트 → 문자열 변환 시 사용
'구분자'.join(리스트)
'''
# words = ["빅데이터", "머신러닝", "딥러닝"]
# print(" ".join(words))
# '빅데이터 머신러닝 딥러닝'

# print("-".join(words))
# '빅데이터-머신러닝-딥러닝'

# 6. 공백 제거 (strip, lstrip, rstrip)
# text = "   파이썬   "
#
# print(text.strip())   # '파이썬' (양쪽 공백 제거)
# print(text.lstrip())  # '파이썬   ' (왼쪽만 제거)
# print(text.rstrip())  # '   파이썬' (오른쪽만 제거)

# 7. 대소문자 변환
# msg = "Python Programming"
#
# print(msg.upper())   # 'PYTHON PROGRAMMING'
# print(msg.lower())   # 'python programming'
# print(msg.title())   # 'Python Programming'
# print(msg.swapcase())# 'pYTHON pROGRAMMING'

# 8. 문자열 검색
# text = "빅데이터 분석기사 파이썬 공부"
#
# print(text.find("분석"))   # 4 (첫 위치 반환, 없으면 -1)
# print(text.index("분석"))  # 4 (없으면 오류 발생)
# print(text.count("파이썬")) # 1 (등장 횟수)

# 9. 정리
'''
replace(): 문자열 교체
슬라이싱 [start:end:step]: 부분 문자열 추출
split() / join(): 문자열 ↔ 리스트 변환
strip(): 공백 제거
upper()/lower(): 대소문자 변환
find()/count(): 검색 및 개수 확인
'''

# 미니 실습 문제

# 문제 1
'''
문자열 "빅데이터 분석기사 파이썬 공부"에서
"공부"를 "스터디"로 바꿔 출력하시오.
'''
# text1 = "빅데이터 분석기사 파이썬 공부"
# print(text1.replace("공부", "스터디"))

# 문제 2
'''
문자열 "빅데이터 분석기사 파이썬 공부"에서
"분석기사"를 "분석을 위한"으로,
"파이썬"을 "머신러닝"으로 변경하시오.
'''
# text2 = "빅데이터 분석기사 파이썬 공부"
# print(text2.replace("분석기사", "분석을 위한",).replace("파이썬", "머신러닝"))

# 문제 3
'''
문자열 "안녕하세요! 함께 성장해요."에서
- 처음 두 글자를 출력
- "함께"만 출력
- 문자열 전체를 거꾸로 출력하시오.
'''
# text3 = "안녕하세요! 함께 성장해요."
# print(text3[:2])
# print(text3[7:9])
# print(text3[::-1])

# 문제 4
'''
날짜 문자열 "2022-12-25"에서
- 월-일 부분만 슬라이싱하여 출력하시오.
- split('-')를 이용해 리스트로 변환하시오.
'''
# date = "2022-12-25"
# print(date[5:])
# print(date.split("-"))

# 문제 5
'''
리스트 ["빅데이터", "머신러닝", "딥러닝"]을
- 공백(" ")으로 join하여 하나의 문자열로 출력하시오.
- 하이픈("-")으로 join하여 출력하시오.
'''
li1 = ["빅데이터", "머신러닝", "딥러닝"]
# print(" ".join(li1))
# print("-".join(li1))



#------------------
# 함수
#------------------
# 1. 기본 함수 정의와 호출
'''
def 함수이름(): 으로 정의
호출 시 함수이름() 형태로 사용
'''
# def greeting():
#     print("파이썬 함수 시작!")
#
# # 함수 여러 번 호출
# greeting()
# greeting()

# 2. 매개변수(Parameter) 있는 함수
'''
외부에서 값을 전달받아 사용 가능
'''
# def greet(name):
#     print("안녕하세요,", name)
#
# greet("철수")
# greet("영희")

# 3. 여러 매개변수 사용
'''
두 개 이상의 인자도 전달 가능
'''
# def add(x, y):
#     print("두 수의 합:", x + y)
#
# add(10, 20)   # 30
# add(7, 5)     # 12

# 4. 리턴(Return) 있는 함수
'''
return 키워드로 결과 반환
함수 호출 결과를 변수에 저장 가능
'''
# def multiply(x, y):
#     return x * y
#
# result = multiply(6, 7)
# print(result)   # 42

# 5. 여러 값 반환
'''
함수에서 튜플 형태로 여러 값 반환 가능
'''
# def min_max(numbers):
#     return min(numbers), max(numbers)
#
# nums = [3, 9, 1, 7, 5]
# small, large = min_max(nums)
# print("최솟값:", small)
# print("최댓값:", large)

# def multiply(x,y):
#     return x * y, x+y, x if x > y else y-x
#
# result = multiply(6,7)
# print(result)

# 6. 평균 함수
# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# scores = [80, 90, 70, 100]
# print("평균:", average(scores))   # 85.0

# 7. 기본값 매개변수 (default parameter)
'''
인자를 전달하지 않으면 기본값 사용
'''


# def introduce(name, age=20):
#     print(f"이름: {name}, 나이: {age}")
#
# introduce("홍길동", 25)
# introduce("김철수")   # 나이는 기본값 20 사용

# 8. 가변 매개변수 (*args)
'''
개수가 정해지지 않은 인자 처리 가능
'''
# def total(*args):
#     return sum(args)
#
# print(total(1, 2, 3))       # 6
# print(total(5, 10, 15, 20)) # 50

# 9. 키워드 매개변수 (**kwargs)
'''
딕셔너리 형태로 인자를 받아 처리
'''
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
#
# show_info(name="Alice", age=25, city="Seoul")

# 10. 정리
'''
def로 함수 정의, return으로 값 반환
매개변수 → 기본값, 가변 인자(*args, **kwargs) 활용 가능
함수는 코드 재사용성과 가독성을 높이는 핵심 요소
'''


# 문제 1
'''
함수 greet()을 정의하여 "파이썬 함수 시작!"을 출력하고,
세 번 호출하시오.
'''
# def greet():
#     print("파이썬 함수 시작!")
#
# greet()
# greet()
# greet()

# 문제 2
'''
이름을 매개변수로 받아
"안녕하세요, [이름]"을 출력하는 함수 hello(name)을 작성하고
"철수", "영희"로 각각 호출하시오.
'''
# def hello(name):
#     print(name)
#
# hello("철수")
# hello("영희")


# 문제 3
'''
두 수를 입력받아 합을 반환하는 함수 add(x, y)를 작성하고,
결과를 변수에 저장하여 출력하시오.
'''
# def add(x, y):
#     return x+y
#
# result = add(25,26)
# print(result)

# 문제 4
'''
리스트 [3, 8, 1, 7, 5]에서
최솟값과 최댓값을 반환하는 함수 min_max(data)를 작성하시오.
'''
# def min_max(data):
#     print("최솟값 : ",min(data))
#     print("최댓값 : ",max(data))
#
#
# li = [3, 8, 1, 7, 5]
# min_max(li)

# 문제 5
'''
여러 개의 숫자를 인자로 받아 총합을 구하는 함수 total(*args)를 작성하고,
(1,2,3), (10,20,30,40)을 각각 전달해 결과를 출력하시오.
'''
# def total(*args):
#
#     return sum(*args)
#
# t1 = (1,2,3)
# t2 = (10,20,30,40)
# print(total(t1))
# print(total(t2))


