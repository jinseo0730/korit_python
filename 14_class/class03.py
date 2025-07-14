#Person => age, email, name /// name은 기본값으로 홍길동
#introduce 메소드 => 자신을 소개하는 메소드
class Person:
    def __init__(self, age, email, name="홍길동"):
        self.age = age
        self.email = email
        self.name = name
        print(f"나이: {self.age}, 이메일: {self.email}, 이름: {self.name}")

    def introduce(self):
        print(f"저의 이름은 {self.name}이고\n나이는 {self.age}살이며\n이메일은 {self.email}입니다.")

person1 = Person(23, "jsbae0373@naver.com", "배진서")
person1.introduce()

person2 = Person(20, "gildonghong@gmail.com")
person2.introduce()

person2.address = "부산 진구" #person2 객체에 address라는 새로운 속성을 추가
print(person2.address)

setattr(person1, "address", "부산 중구") #속성 추가
print(person1.address)
