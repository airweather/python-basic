# 내장함수
# 파이선 인터프리터에서 기본적으로 지원하는 함수

# 최대값
# print(max(2,3,4))

# 최소값
# print(min(2,3,4))

# 정수
# print(round(3.14))

# 절대값
# print(abs(-3))

# 거듭제곱(2^3)
# print(pow(2,3))

# 함수
# 특정 작업을 수행하는 명령문의 집합

# 사용자 정의 함수
# 내장 함수와 달ㅣ 사용자의 목적에 따라 정의된 함수

# 반환값에 따른 함수의 종류
# 반환값이 없는 함수 : print
# 반환값이 있는 함수 : input, format, int등


# 반환값이 없는 함수 정의
# def 함수이름(매개변수 리스트):
#     명령 블록



# 숫자 역순 출력 프로그램

# def reverse_number(num):
#     while num !=0:
#         digit = num % 10
#         num = num // 10
#         print(digit, end="")

# num = int(input("역순으로 출력할 숫자를 입력하세요 :"))
# reverse_number(num)

# format함수의 실수 데이터 형식화
# >10.2f
# > : 정렬방향, 10 : 필드 폭, .2 : 소숫점 이하 자리 수, f : 데이터 타입

# number = 12345.6789
# print(format(number, ">10.3f"))


