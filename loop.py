# 반복 구조 설계 전략
# 1. 반복되어야 하는 명령 블록을 작성
# 2. 반복되어야 하는 명령문을 다음과 같이 반복 구조로 작성
#     while True:
#         명령 블록
# 3. 반복-계속-조건을 작성하고 반복 구조를 제어하기 위해 반복 제어 명령문을 추가
#     while 반복-계속-조건:
#         명령 블록
#         반복 제어 명령문


# 구구단
i = 1
base = int(input("출력할 단을 입력하세요 : "))

while i <=9:
    print(base, "X", i, "=", base * i)
    i = i+1

# 계수 제어 반복(for loop)

hei_list = [1, 4, 14, 26, 31]
for hei in hei_list :
    print(hei)