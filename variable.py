# 동시할당
# 복수개의 변수에 값을 동시에 할당
temp, season = 27, "summer"

# 교환(swap)
# 복수 개의 변수에 할당하는 값을 맞바꿈
temp, season = season, temp

# 세 개의 값을 입력받아 오름차순으로 정렬하는 함수
a = int(input("첫번째 숫자를 입력하세요:"))
b = int(input("두번째 숫자를 입력하세요:"))
c = int(input("세번째 숫자를 입력하세요:"))

def sort3(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
