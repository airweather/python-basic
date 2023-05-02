temp = 20
fruit = "apple"

# AND
# AND연산은 and
print(temp >= 27 and fruit =="pear")
print(temp >= 27 and fruit =="apple")
print(temp >= 19 and fruit =="apple")

# OR
# OR연산은 or
print(temp >= 27 or fruit =="pear")
print(temp >= 27 or fruit =="apple")
print(temp >= 19 or fruit =="apple")

# NOT - 단항 연산자로 논리반전
# not을 붙임
print(temp <= 27)
print(not temp <= 27)

# shor-circuit evaluation
# 첫 번째 논리값 만으로 전체 연산 결과가 판별 가능할 때 두 번째 논리값은 확인(평가)하지 않는 기법

