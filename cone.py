# 반지름 40, 높이 10
# rad = int(input("반지름을 입력하세요 : "))
# hei = int(input("높이를 입력하세요 : "))
# hei_list = [1, 5, 14, 26, 31]

# for hei in hei_list :
#     vol = 1/3 * 3.14 * rad ** 2 * hei
#     print("부피는 : ", vol, "입니다.")

#     #겉넓이 계산 출력
#     suf = 3.14 * rad ** 2 + 3.14 * rad * hei
#     print("원뿔의 넓이는 : ",suf,"입니다.")



#python은 4칸을 들여쓰기 해주면 블럭이 지정됨
# if rad > 0 and hei > 0:
#     # 부피 계산 출력
#     vol = 1/3 * 3.14 * rad ** 2 * hei
#     print("부피는 : ", vol, "입니다.")

#     #겉넓이 계산 출력
#     suf = 3.14 * rad ** 2 + 3.14 * rad * hei
#     print("원뿔의 넓이는 : ",suf,"입니다.")
# else : 
#     print("반지름과 높이의 값을 모두 양수로 입력해주세요")



# range함수 (초기값, 최종값-1, 증가량)
rad_list = range(10, 31, 10)
hei_list = [1, 5, 14]

# zip() 함수 : 여러 리스트의 값들을 하나씩 엮어서 가져오는 함수
for rad, hei in zip(rad_list, hei_list) :
    vol = 1/3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("반지름", rad, "높이", hei, "원뿔 ")
    print("원뿔의 부피는 : ", vol, "입니다.")
    print("원뿔의 넓이는 : ",suf,"입니다.")

    