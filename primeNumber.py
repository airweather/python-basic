import time

start_time = time.time()

def is_prime(number) :
    
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

prime_count = 0

for i in range(2, 5001):
    if is_prime(i) :
        prime_count = prime_count + 1
        print(i, end=", ")

end_time = time.time()
print("\n",end_time-start_time, "초 실행했습니다.")