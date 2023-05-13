import random
import math

guess_str = input("로또 번호 6개를 쉼표로 분리하여 입력하세요: ").split(",")
guess_list = list()

for i in guess_str:
    guess_list.append(int(i))

# range(시작숫자, 마지막 숫자, 출력 수)
lotto_list = random.sample(range(1, 46, 1), 6)

print("예상 번호는", guess_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.")

hit_count = 0

for guess in guess_list:
    if guess in lotto_list:
        hit_count = hit_count + 1

print("축하합니다" + str(hit_count) + "개 맞췄습니다.")