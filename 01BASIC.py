# -----------------------
# 주석1
# -----------------------
'''
다
중
렬
주
석
처
리
'''

# ctrl + / 단축키
# -----------------------
# 출력함수(생략)
# -----------------------

# -----------------------
# 입력함수
# -----------------------
# name = input("이름을 입력하세요 : ")
# print("입력한 이름 : ", name)
# print("자료형 : ", type(name))
# 이름을 입력하세요 : 웅애웅
# 입력한 이름 :  웅애웅
# 자료형 :  <class 'str'>


# 숫자 입력
# age = int(input ("나이를 입력하세요 : "))
# print("내년 나이 : ", age + 1)
# 나이를 입력하세요 : 15
# 내년 나이 :  16
# int형변환 안할 시 : TypeError: can only concatenate str (not "int") to str

# Python의 기본 파일 자료는 class
# 실행 단축키 : Shift + F10

# -----------------------
# 변수
# -----------------------
# # 1) 변수 선언과 값 대입
# age = 39
# height = 1.75
# name = "Alice"
#
# #  변수 출력
# print(name)
# print(age)
# print(height)
# # Alice
# # 39
# # 1.75
# print(type(name))
# print(type(age))
# print(type(height))
# # <class 'str'>
# # <class 'int'>
# # <class 'float'>
#
#
# # 여러 변수 출력
# print("name:", name, "age:", age, "height:", height)
# name: Alice age: 39 height: 1.75
# # , : 띄어쓰기를 기본 원칙으로 한다.
#
# # 문자열 포매팅 (f-string) like 서식문자
# print(f"[f-string] {name} - age={age}, height={height}")
# [f-string] Alice - age=39, height=1.75
#
# # 자료형 확인
# print(type(name))   # <class 'str'>
# print(type(age))    # <class 'int'>
# print(type(height)) # <class 'float'>
#
# # 변수 재할당
# age = 40
# print("새 나이:", age)
# # 새 나이: 40
# # age = "40세"
# print("새 나이:", age)
# print(type(age))
# # 새 나이: 40세
# # <class 'str'>
# # 변경된 자료형으로 변환
#
# # 변수 삭제
# del age
# # C++에 있는거임
# print(age)
# # 오류 발생: age is not defined```
#
# # ------------------------
# # ------------------------
# # 1) 여러 변수에 한 줄 대입
# x, y, z = 10, 20, 30
# print(x, y, z)
# # 10 20 30
#
# # 같은 값 대입
# a = b = c = 100
# print(a, b, c)
# # 100 100 100
#
# # 값 교환 (스왑)
# x, y = y, x
# print("스왑 후:", x, y)
# # 스왑 후: 20 10
#
# # 언패킹 (리스트/튜플 분해)
# numbers = [1, 2, 3]
# n1, n2, n3 = numbers
# print(n1, n2, n3)
# # 1 2 3
#
# # 확장 언패킹 (*)
# first, *rest = [10, 20, 30, 40, 50]
# print(first)   # 10
# print(rest)    # [20, 30, 40, 50]
#
# # 언패킹 응용: 마지막 값 따로 받기
# *start, end = [100, 200, 300, 400]
# print(start, end)  # [100, 200, 300] 400```

# # 미니문제
# '''
# a = 1, b = 2, c = 3을 선언한 뒤, 한 줄로 a=2, b=3, c=1이 되도록 바꾸기.
# 리스트 [5,10,15,20,25]에서 처음 두 값은 x, y 나머지는 rest로 분리해 출력하기.
# m=100, n=200일 때, m과 n을 교환하고 두 값의 합을 출력하기.
# '''
# print("---------------")
# a, b, c = 1, 2, 3
# a, b, c = b, c, a
# print(a,b,c)
# print("---------------")
# number = [5,10,15,20,25]
# first, second, *rest = number
# print(first,second,rest)
# print("---------------")
# m , n = 100, 200
# m, n = n, m
# print(m, n, m+n)
# print("---------------")

# -----------------------
# 형변환
# -----------------------
# 1단계) 숫자 ↔ 문자열 변환
# 문자열 -> 정수
# a = int("10")
# print(a,type(a))
# 10 <class 'int'>

# 문자열 -> 실수
# b = float("3.14")
# print(b, type(b))
# 3.14 <class 'float'>

# 숫자 -> 문자열
# c = str(123)
# print(c, type(c))
# 123 <class 'str'>

'''
미니 문제
1. 문자열 `"123"`을 정수로 변환해 +1 한 결과를 출력하시오.  
2. 문자열 `"3.5"`를 실수로 변환해 +1 한 결과를 출력하시오.  
3. 숫자 `2025`를 문자열로 변환해 `"년"`과 결합하여 `2025년`을 출력하시오.  
'''

# 2단계) 불리언 변환
# print(bool(0))      # False
# print(bool(1))      # True
# print(bool(""))     # False (빈 문자열)
# print(bool("0"))    # True  (문자열 "0"은 내용이 있으므로 True)
# print(bool([]))     # False (빈 리스트)
# print(bool([1]))    # True

'''
미니 문제
1. `bool(0)`, `bool("")`, `bool("Python")`의 결과를 각각 확인하시오.  
2. 리스트 `[]`와 `[1]`을 `bool()`로 변환했을 때 차이를 확인하시오.  
'''

# 3단계) 컬렉션 변환
# data = [1, 2, 2, 3]

# list → set (중복 제거)
# s = set(data)
# print(s, type(s))   # {1,2,3} <class 'set'>

# set → list 값 변경 가능
# l = list(s)
# l[0] = 100
# print(l, type(l))   # [100,2,3] <class 'list'>

# tuple 변환  값 변경 불가능
# t = tuple(data)
# print(t, type(t))   # (1, 2, 2, 3) <class 'tuple'>

'''
미니 문제
1. 리스트 `[1, 2, 2, 3]`을 집합(set)으로 변환해 출력하시오.  
2. 집합 `{1, 2, 3}`을 리스트로 변환하고 인덱스로 첫 번째 값을 출력하시오.  
3. 리스트 `[10, 20, 30]`을 튜플로 변환하여 출력하시오.  
'''

# 4단계) dict 변환
# d = {"a": 1, "b": 2, "c": 3}
# print("!", d, type(d))
# ! {'a': 1, 'b': 2, 'c': 3} <class 'dict'>

# 키만 리스트로
# keys = list(d)
# print(keys)   # ['a', 'b', 'c']

# 값만 리스트로
# values = list(d.values())
# print(values) # [1, 2, 3]

# 키-값 쌍 튜플로
# items = list(d.items())
# print(items)  # [('a',1), ('b',2), ('c',3)]

'''
미니문제
1. 딕셔너리 `{"a": 1, "b": 2}`에서 키 목록을 리스트로 변환해 출력하시오.  
2. 같은 딕셔너리에서 값 목록을 리스트로 변환해 출력하시오.  
3. 키-값 쌍을 튜플 리스트 형태로 변환해 출력하시오.  
'''
# di = {"a": 1, "b": 2}
# keys = list(di)
# values = list(di)
# items = list(di.items())
# print(keys)
# print(values)
# print(items)


# 5단계) 종합 실습
# 사용자 입력(문자열) → 숫자 변환
# year = int("2025")
# month = int("9")
# day = int("8")
#
# date = f"{year:04d}-{month:02d}-{day:02d}"
# print(date)   # 2025-09-08

'''
미니문제
문자열 `"2025"`, `"09"`, `"08"`을 각각 정수로 변환하여  
형식 `2025-09-08`로 출력하시오. (월, 일은 두 자리로 맞출 것)  
'''

# year = int("2025")
# month = int("9")
# day = int("9")

# date = f"{year:04d}-{month:02d}-{day:02d}"
# print(date)
# 2025-09-09


# -----------------------
# 연산자
# -----------------------
# 1) 산술 연산자 예시
# 덧셈, 뺄셈, 곱셈, 나눗셈
# a, b = 7, 2
# print("a + b =", a + b)    # 9
# print("a - b =", a - b)    # 5
# print("a * b =", a * b)    # 14
# print("a / b =", a / b)    # 3.5  (항상 실수)

# 몫, 나머지, 거듭제곱
# print("a // b =", a // b)  # 3
# print("a % b  =", a % b)   # 1
# print("2 ** 3 =", 2 ** 3)  # 8

# 2) 비교 연산자 예시
# x, y = 5, 3
# print("x == y :", x == y)   # False
# print("x != y :", x != y)   # True
# print("x >  y :", x > y)    # True
# print("x <  y :", x < y)    # False
# print("x >= y :", x >= y)   # True
# print("x <= y :", x <= y)   # False

# 체이닝(파이썬만의 문법) //JAVA에서는 안 됨
# n = 4
# print(3 < n < 10)    # True (3 < n and n < 10)

# 3) 논리 연산자 예시
# a, b = True, False
# print("a and b :", a and b)    # False
# print("a or  b :", a or b)     # True
# print("not a   :", not a)      # False
'''
and != &&
or != ||
not != ! 
'''

# 단락 평가(short-circuit) 예시
# def f():
#     print("f() called")
#     return True

# print(False and f())  # False (f()는 호출되지 않음)
# print(True or f())    # True  (f()는 호출되지 않음)

# 4) 대입/복합 대입 연산자 예시
# x = 10      # 대입
# x += 5      # 15
# x -= 3      # 12
# x *= 2      # 24
# x /= 4      # 6.0 (실수 주의)
# x //= 2     # 3
# x %= 2      # 1
# x **= 5     # 1 ** 5 = 1
# print("x =", x)

# 문자열/리스트에도 사용 가능
# s = "ha"
# s *= 3    # s = "ha"*3
# print(s)    # "hahaha"

# arr = [1]
# arr *= 3    # [1]*3
# print(arr)  # [1, 1, 1]

# 5) 비트 연산자 예시
# a, b = 6, 3                 # a=0b110, b=0b011
# print("a & b =", a & b)     # 2  (0b010)
# print("a | b =", a | b)     # 7  (0b111)
# print("a ^ b =", a ^ b)     # 5  (0b101)

# 비트 NOT: ~n = -(n+1)
# print("~6 =", ~6)           # -7

# 시프트
# print("3 << 1 =", 3 << 1)   # 6
# print("6 >> 1 =", 6 >> 1)   # 3

# 2진수로 보기 좋게 출력
# n = 13
# print("n      :", n, bin(n))         # 13 0b1101
# print("n<<2   :", n << 2, bin(n<<2)) # 52 0b110100
# print("n>>1   :", n >> 1, bin(n>>1)) # 6  0b110

# 6) 멤버십/식별 연산자 예시
# 멤버십: in / not in
# text = "apple"
# print("'a' in text     :", "a" in text)      # True
# print("'x' not in text :", "x" not in text)  # True

# nums = [1, 2, 3]
# print("2 in nums      :", 2 in nums)         # True
# print("4 not in nums  :", 4 not in nums)     # True

# 식별: is / is not  (객체 동일성)
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print("a == b  :", a == b)    # 값(내용)은 같다 -> True
# print("a is b  :", a is b)    # 객체(참조)는 다르다 -> False
# print("a is c  :", a is c)    # 같은 객체 참조 -> True

# 작은 정수/짧은 문자열 캐싱으로 is가 True처럼 보일 수 있으니 ==와 구분할 것
# s1 = "py"
# s2 = "py"
# print("s1 == s2:", s1 == s2)  # True (값 비교)
# print("s1 is s2:", s1 is s2)  # (환경별 최적화 영향) 동일성 보장은 아님

# 6) 멤버십/식별 연산자 예시
# 멤버십: in / not in  #포함 미포함
# text = "apple"
# print("'a' in text     :", "a" in text)      # True
# print("'x' not in text :", "x" not in text)  # True

# nums = [1, 2, 3]
# print("2 in nums      :", 2 in nums)         # True
# print("4 not in nums  :", 4 not in nums)     # True

# 식별: is / is not  (객체 동일성)
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print("a == b  :", a == b)    # 값(내용)은 같다 -> True
# JAVA에서는 참조값을 비교하지만 PYTHON에서는 값을 비교하는거다.
# print("a is b  :", a is b)    # 객체(참조)는 다르다 -> False
# print("a is c  :", a is c)    # 같은 객체 참조 -> True

# 작은 정수/짧은 문자열 캐싱으로 is가 True처럼 보일 수 있으니 ==와 구분할 것
# s1 = "py"
# s2 = "py"
# print("s1 == s2:", s1 == s2)  # True (값 비교)
# print("s1 is s2:", s1 is s2)  # (환경별 최적화 영향) 동일성 보장은 아님

'''
과제(1,2,4,5번 풀기)
1.평균 계산
변수 score_kor=88, score_eng=92, score_math=79를 사용하여 평균을 구한 뒤 avg를 출력하시오.
평균은 실수로 계산할 것.

2.합격 판정
조건: avg >= 90 이고 세 과목 점수가 모두 >= 70이면 passed=True, 아니면 False.
결과를 print("passed:", passed)로 출력하시오.

3.비트 마스크 권한 토글
읽기=1, 쓰기=2, 실행=4 를 각각 READ, WRITE, EXEC로 두고 perm=0에서 시작.
읽기와 실행 권한을 추가(|= 사용)한 뒤 perm과 bin(perm)을 출력.
실행 권한 보유 여부를 비트 연산으로 확인하여 불리언으로 출력하시오.

4.멤버십 검사
리스트 users = ["kim", "lee", "park"]에서 "lee"가 포함되어 있는지 in으로 검사해 출력하시오.

5.식별 연산자 검사
x = [1, 2]; y = x; z = [1, 2] 일 때, x is y와 x is z 결과를 각각 출력하시오.
'''

# 문제 1) 변수 score_kor=88, score_eng=92, score_math=79를 사용하여 평균을 구한 뒤 avg를 출력하시오.
# 평균은 실수로 계산할 것.
# score_kor = 88
# score_eng = 92
# score_math = 79
# avg = (score_math + score_eng + score_kor) / 3
# print(f"{avg:.2f}")

# 문제 2) 조건: avg >= 90 이고 세 과목 점수가 모두 >= 70이면 passed=True, 아니면 False.
# 결과를 print("passed:", passed)로 출력하시오.
# passed = (avg >= 90) and (score_kor <= 70) and (score_eng >= 70) and (score_math >= 70)
# print("passed:", passed)

# 문제 4) 리스트 users = ["kim", "lee", "park"]에서 "lee"가 포함되어 있는지 in으로 검사해 출력하시오.
# users = ["kim", "lee", "park"]
# print("lee" in users)

# 문제 5) x = [1, 2]; y = x; z = [1, 2] 일 때, x is y와 x is z 결과를 각각 출력하시오.
# x = [1, 2]
# y = x
# z = [1, 2]
# print("x is y : ", x is y)
# print("x is z : ", x is z)

# -----------------------
# 분기분
# -----------------------
# 1단계) 기본 if 문
# x = 10

# if x > 5:
#     print("x는 5부다 크다")  # 조건이 True라면 실행
#     print("TEST")

# if x > 5:
#     print("x는 5보다 크다")
#     print("TEST")
#     print("TEST")

# 2단계) if-else 문
# score = 65

# if score >= 70:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")

# 3단계) if-elif-else 문
# num = 0

# if num > 0:
#     print("양수")
# elif num < 0:
#     print("음수")
# else:
#     print("0입니다.")

# 4단계) 중첩 if 문
# age = 20
# has_ticket = True

# if age >= 18:
#     if has_ticket:
#         print("입장 가능합니다.")
#     else:
#         print("티켓이 필요합니다.")
# else:
#     print("미성년자는 입장 불가")

# 5단계) 조건 표현식 (삼항 연산자)
# score = 85

# result = "합격" if score >= 60 else "불합격"
# print(result)   # 합격

# 6단계) 논리 연산자와 함께 사용
# age = 25
# is_student = True

# if age >= 20 and is_student:
#     print("성인 학생입니다.")

# 7단계) in 연산자 활용
# fruit = "apple"

# if fruit in ["apple", "banana", "cherry"]:
#     print(f"{fruit}은(는) 과일 목록에 있습니다.")

# 8단계) pass 문
# JAVA에서는
# if True
#     ;

# x = 10

# if x > 0:
#     pass   # 아직 로직 미작성, 오류 없이 넘어감
# else:
#     print("x는 0 이하")

# 9단계) 예외적인 케이스 처리
# value = input("숫자를 입력하세요: ")

# if value.isdigit():
#     num = int(value)
#     print("입력한 숫자:", num)
# else:
#     print("숫자가 아닙니다.")

# 10단계) 종합 실습
# 시험 점수를 입력받아 등급 출력하기
# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"당신의 학점은 {grade} 입니다.")

'''
정리
if: 조건이 True일 때 실행
if-else: 조건이 True/False일 때 각각 실행
if-elif-else: 여러 조건을 순차적으로 검사
중첩 if: 조건문 안에서 또 다른 조건 검사
조건 표현식: 한 줄로 간단히 참/거짓에 따라 값 결정
pass: 조건문 뼈대를 먼저 작성할 때 사용
'''

# 미니 실습 문제
# 문제1)
'''
사용자로부터 나이와 학생 여부(yes/no)를 입력받아  
- 나이가 20세 이상이고 학생이면 "성인 학생"  
- 나이가 20세 이상이고 학생이 아니면 "성인 비학생"  
- 나이가 20세 미만이면 "미성년자"  
를 출력하는 프로그램을 작성하시오.
'''
# userage = int(input("나이를 입력하세요 : "))
# userisstudent = input("학생이십니까?(yes or no) : ")
#
# if userage >= 20 and "yes" in userisstudent :
#     print("성인 학생")
# elif userage >= 20 and "no" in userisstudent :
#     print("성인 비학생")
# else:
#     print("미성년자")

# 문제2)
'''
정수를 입력받아  
- 3의 배수이면서 5의 배수이면 "3과 5의 공배수"  
- 3의 배수이면 "3의 배수"  
- 5의 배수이면 "5의 배수"  
- 그 외는 "해당 없음"  
을 출력하는 코드를 작성하시오.
'''
# num = int(input("정수를 입력하세요 : "))
# if num%3==0 and num%5==0 :
#     print(num,"는 3과 5의 공배수")
# elif num%3==0 :
#     print(num,"는 3의 배수")
# elif num%5==0 :
#     print(num,"는 5의 배수")
# else :
#     print("해당 없음")

# 문제3번
'''
정수를 입력받아  
- 양수이면서 짝수 → "양의 짝수"  
- 양수이면서 홀수 → "양의 홀수"  
- 음수이면 "음수"  
- 0이면 "0"  
을 출력하는 코드를 작성하시오.
'''
# num = int(input("정수를 입력하세요 : "))
# if num==0:
#     print("0")
# elif num<0:
#     print("음수")
# elif num>0 and num%2==0:
#     print("양의 짝수")
# else:
#     print("양의 홀수")

# 문제 5
'''
쇼핑몰에서 구매 금액을 입력받아  
- 100,000원 이상 → "10% 할인 적용"  
- 50,000원 이상 → "5% 할인 적용"  
- 그 외 → "할인 없음"  
을 출력하는 프로그램을 작성하시오.
'''
# money = int(input("구매 금액을 입력하세요 : "))
# if money >= 100000:
#     print("10% 할인 적용")
# elif money >= 50000:
#     print("5% 할인 적용")
# else:
#     "할인 없음"



# -----------------------
# 반복문
# -----------------------
# 1단계) 기본 for문
# 리스트 반복
# fruits = ["apple", "banana", "cherry"]

# for f in fruits:
#     print(f)
# apple
# banana
# cherry

# 2단계) range() 활용
# range(strat : stop : step) !!stop-1!!
# 0부터 4까지 출력
# for i in range(5):
#     print(i)

# 1부터 10까지 홀수 출력
# for i in range(1, 11, 2):
#     print(i)

# 3단계) while문
# count = 0

# while count < 5:
#     print("count =", count)
#     count += 1

# 4단계) break / continue
# break 예시
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)   # 1~4 출력

# continue 예시
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)   # 1, 2, 4, 5 출력

# 5단계) 중첩 반복문
# for i in range(1, 4):       # 행
#     for j in range(1, 4):   # 열
#         print(f"({i},{j})", end=" ")
#     print()

# 6단계) else와 함께 쓰는 반복문
# for문과 else
# for n in range(2, 5):
#     if n % 2 == 0:
#         print("짝수 발견:", n)
#         break
# else:
#     print("짝수 없음")

# while문과 else
# x = 3
# while x > 0:
#     x -= 1
#     print("x =", x)
# else:
#     print("루프 종료")

# 7단계) 리스트 컴프리헨션
# 1~5 제곱수 리스트
# squares = [x**2 for x in range(1, 6)]
# print(squares)   # [1, 4, 9, 16, 25]

# 조건부 컴프리헨션 (짝수만)
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)     # [0, 2, 4, 6, 8]

# 8단계) enumerate() 사용 (열거)
# names = ["kim", "lee", "park"]

# for i, name in enumerate(names, start=1):
#     print(i, name)
# 1 kim
# 2 lee
# 3 park
'''
[열거형 in java]

enum ROLE
{
 ROLE_USER,     -0
 ROLE_MANAGER,  -1
 ROLE_ADMIN     -2
}
ROLE.ROLE_USER  -0

'''


# 정리
'''
for문: 시퀀스나 range 순회
while문: 조건이 True일 동안 반복
break: 루프 중단
continue: 다음 반복으로 건너뜀
else: 루프 정상 종료 시 실행
컴프리헨션: 리스트/집합/딕셔너리를 간결하게 생성 가능
'''

# 문제 1
'''
1부터 10까지의 정수를 for문을 사용해 한 줄에 출력하시오.
출력: 1 2 3 4 5 6 7 8 9 10
'''
# for i in range(1, 11):
#     print(i, end=" ")

# 문제 2
'''
리스트 [3, 7, 2, 9, 4]의 합을 for문을 사용해 구하시오.
'''
# li = [3, 7, 2, 9, 4]
# sum = 0
# for i in li:
#     sum += i
#
# print(sum)

# 문제 3
'''
while문을 사용하여 5부터 1까지 거꾸로 출력하시오.
출력: 5 4 3 2 1
'''
# count = 5
#
# while count > 0:
#     print(count, end=" ")
#     count -= 1


# 문제 4
'''
for문과 if문을 사용하여 1부터 20까지 수 중에서 짝수만 출력하시오.
'''
# for i in range(1, 21):
#     if i%2==0:
#         print(i, end=" ")


# 문제 5
'''
구구단 3단을 for문을 사용해 출력하시오.
출력:
3 x 1 = 3
3 x 2 = 6
...
3 x 9 = 27
'''
# for i in range(9):
#     print(3,"X",i+1,"=",3*(i+1))

# 문제 6
'''
구구단 전체 출력해보기
'''
# for dan in range(2, 10):     # 1dan부터 9dan까지
#     print("---",dan,"단---")
#     for j in range(2, 10):
#         print(dan,"X",j,"=",dan*j)
#     print("")

# 문제 7
'''
*
**
***
****
*****
'''
# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print("")

# -----------------------
#
# -----------------------

