# 반지름 40, 높이 10
rad = int(input("반지름을 입력하세요 : "))
hei = int(input("높이를 입력하세요 : "))

#python은 4칸을 들여쓰기 해주면 블럭이 지정됨
if hei > 0 :
    # 부피 계산 출력
    print("부피는 : ", 1/3 * 3.14 * rad ** 2 * hei, "입니다.")

    #겉넓이 계산 출력
    print(3.14 * rad ** 2 + 3.14 * rad * hei)
else : 
    print("반지름에 양수값을 넣어주세요")