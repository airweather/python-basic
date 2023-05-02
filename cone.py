# 반지름 40, 높이 10
rad = int(input("반지름을 입력하세요 : "))
hei = int(input("높이를 입력하세요 : "))

#python은 4칸을 들여쓰기 해주면 블럭이 지정됨
if rad > 0 :
    # 부피 계산 출력
    vol = 1/3 * 3.14 * rad ** 2 * hei
    print("부피는 : ", vol, "입니다.")

    #겉넓이 계산 출력
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("원뿔의 넓이는 : ",suf,"입니다.")
else : 
    print("반지름에 양수값을 넣어주세요")