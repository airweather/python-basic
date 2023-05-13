# 스무고개
# 1 ~ 1000사이의 숫자 맞추기

import random

hit_number = random.randint(1, 1000)

guess_count_list = range(1, 21, 1)

passfail = False

for guess_count in guess_count_list:
    
    guess = int(input("숫자를 맞혀보세요("+str(guess_count)+"번째 시도)"))

    if hit_number == guess:
        passfail = True
        break
    elif hit_number > guess:
        print(str(guess) + "보다 큽니다.", end="")
    else :
        print(str(guess) + "보다 작습니다.", end="")

if passfail == True:
    print("맞췄습니다. 축하합니다.")
else:
    print("모든 기회를 다 사용하셨습니다. 다음에 다시 도전해 주세요")