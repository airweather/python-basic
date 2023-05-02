# A, B, C 사용자 입력
A = int(input("A 입력 : "))
B = int(input("B 입력 : "))
C = int(input("C 입력 : "))

# A, B, C중 가장 큰 수 출력
if A > B:
    if A > C :
        print(A)
    else :
        print(C)
else :
    if B > C :
        print(B)
    else:
        print(C)
