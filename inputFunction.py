
# input함수

# input함수의 파라미터로 입력 안내 문구를 넣을 수 있음
# rad = input("반지름의 값을 입력하세요 : ")
# print("input : ", rad)

# input함수는 값을 str로 입력받는다
data = input("값을 입력하세요 : ")
print(type(data))

# 형변환
# str() : 문자열 타입으로 변환
# int() : 정수 타입으로 변환
# float() : 소수 타입으로 변환

# 입력받은 값을 int형으로 형변환 후 rad 변수에 입력
rad = int(input("반지름의 값을 입력하세요 : "))

# print함수는 파라미터의 제한이 없다
# 각 파라미터 별 공백 한칸이 생기며 sep=""로 파라미터 별 분류를 변경할 수 있음
print('a', 'b', 'c', sep=" : ")

# 프로그래밍 에러
# 구문 오류(syntax error) : 문법 체계에 적합하지 않은 명령문 입력 시 발생
# 실행 오류(runtime error) : 논리적으로 실행 불가능한 명령문 작성 시 발생
# 의미 오류(semantic error) : 의미적으로 잘못 해석되는 명령문 작성 시 발생