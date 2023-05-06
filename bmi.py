# BMI계산 프로그램

class BMI :
    def __init__(self, name, age, weight, height) :
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def get_BMI(self) :
        return self.weight / (self.height/100) ** 2
    def get_status(self) :
        BMI = self.get_BMI()
        if BMI >= 25 :
            return "비만"
        elif BMI >= 23 and BMI < 25 :
            return "과체중"
        elif BMI >= 18.5 and BMI < 23 :
            return "정상"
        else :
            return "저체중"

person1 = BMI("홍길동",40,78,182)
print(person1.name + "님(" +str(person1.age)+"세)의 BMI 수치는", person1.get_BMI(), "결과는",person1.get_status(), "입니다.")