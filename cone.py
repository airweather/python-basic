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
# rad_list = range(10, 31, 10)
# hei_list = [1, 5, 14]

# zip() 함수 : 여러 리스트의 값들을 하나씩 엮어서 가져오는 함수
# for rad, hei in zip(rad_list, hei_list) :
#     vol = 1/3 * 3.14 * rad ** 2 * hei
#     suf = 3.14 * rad ** 2 + 3.14 * rad * hei
#     print("반지름", rad, "높이", hei, "원뿔 ")
#     print("원뿔의 부피는 : ", vol, "입니다.")
#     print("원뿔의 넓이는 : ",suf,"입니다.")

# 반환값이 없는 함수
# def prt_con_vol(r, h):
#     if r>0 and h>0 :
#         vol = 1/3 * 3.14 * r ** 2 * h
#         print("원뿔의 부피는",vol,"입니다.")
#     else:
#         # r, h가 음수일 때
#         print("반지름과 높이 값에 양수를 입력하세요.")

# rad = 30
# hei = 50
# prt_con_vol(rad, hei)

# 반환값이 있는 함수
# def rtn_cone_vol(r, h):
#     if r>0 and h>0 :
#         vol = 1/3 * 3.14 * r ** 2 * h
#         return vol
#     else:
#         # r, h가 음수일 때
#         print("반지름과 높이 값에 양수를 입력하세요.")

# print(format(rtn_cone_vol(10, 20), ">20.3f"), "입니다.")


# def rtn_cone_vol_surf(r, h):
#     if r>0 and h>0 :
#         vol = 1/3 * 3.14 * r ** 2 * h
#         surf = 3.14 * r ** 2 + 3.14 * r * h
#         return vol, surf
#     else:
#         # r, h가 음수일 때
#         print("반지름과 높이 값에 양수를 입력하세요.")

# vol1, surf1 = (rtn_cone_vol_surf(50, 100))
# print(vol1, "입니다")
# print(surf1, "입니다")


# 값의 전달
# def rtn_cone_vol(r, h):
#     if r>0 and h>0 :
#         # r, h 모두 양수일 때
#         vol = 1/3 * 3.14 * r ** 2 * h
#         surf = 3.14 * r ** 2 + 3.14 * r * h
#         r, h = 0, 0
#         return vol
#     else:
#         # r, h가 음수일 때
#         print("반지름과 높이 값에 양수를 입력하세요.")
    
# radius = 50
# height = 100
# print(format(rtn_cone_vol(radius, height), ">10.3f"))
# print("함수 사용 후 ", radius, height)

# 기본값
# 매개변수에 기본값 설정
# def rtn_cone_vol_surf(r=20, h=30):
#     if r>0 and h>0 :
#         return 1/3 * 3.14 * r ** 2 * h, 3.14 * r ** 2 + 3.14 * r * h
#     else:
#         # r, h가 음수일 때
#         print("반지름과 높이 값에 양수를 입력하세요.")

# print(rtn_cone_vol_surf(100, 20))

# class
class Cone :
    def __init__(self, radius = 20, height = 30):
        self.r = radius
        self.h = height

    def get_vol(self) :
        return 1/3 * 3.14 * self.r ** 2 * self.h
    def get_surf(self) :
        return 3.14 * self.r ** 2 + 3.14 * self.r * self.h

unit_cone = Cone()
big_cone = Cone(50, 100)

print("단위 원뿔의 겉넓이와 부피는", unit_cone.get_surf(), unit_cone.get_vol(), "입니다.")
print("큰 원뿔의 겉넓이와 부피는", big_cone.get_surf(), big_cone.get_vol(), "입니다.")