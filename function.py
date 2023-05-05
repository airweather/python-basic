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


# 값의 전달
# 함수가 호출될 때, 값이 형식 매개변수에 전달(변수가 전달되는 것이 아님)
# x = 1
# print("x의 값은", x)

# def inc(x):
#     x = x + 1
#     print("x의 값은", x)

# inc(x)
# print("x의 값은", x)

# 기본 매개변수
# 함수 호출 시 매개변수가 전달되지 않을 경우 기본값이 전달되는 매개변수
# print()의 sep="", end=""
# 기본 매개변수는 일반 매개변수 앞에 위치할 수 없음

# 기본 매개변수의 정의
# def 함수이름(매개변수 리스트, 매개변수=값 리스트):
#     명령 블록
#     return 반환값 리스트

# 가변 매개변수
# 함수 호출 시 매개변수를 사용자가 원하는 개수 만큼 지정할 수 있는 매개변수
# 매개변수 앞에 "*"
# 일반 매개변수 앞에 위치할 수 없음
# 가변 매개변수는 1개만 사용 가능
# 가변 매개변수는 리스트 형태로 전달
# def 함수이름(매개변수 리스트, *가변 매개변수):
#     명령 블록
#     return 반환값 리스트

def var_sum_avg(*number):
    sum = 0
    count = 0

    for i in number:
        sum = sum + i
        count = count + 1
    return sum, sum/count

print(var_sum_avg(20, 25, 10, 85, 100, 150))
