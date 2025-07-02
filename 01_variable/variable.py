# 주석 처리 (컨트롤 + /)
from operator import truediv

# 변수
# => 어떠한 값들을 상자에 담아 이름을 붙이는 것

#변수 => 문자열
last_name = "김"
print("제 성은 " + last_name)
first_name = "지원"
name = last_name + first_name # 문자열과 문자열은 더할 수 있다. # print 전에는 문자열이 선언되어야 함
print(name)
# a = name - last_name #문자열에서 뺄셈불가
b = name * 3 #문자열을 곱할 수 있다. 단, 나누기는 할 수 없다.
print(b)

#변수 => 정수
age = 21
#변수 => 실수
pie = 3.141592

#변수 => 여러줄을 문자열로 쓸 때
str1 = """
안녕하세요
반갑습니다
"""
str2 = '''
안녕
반가워
''' # str = ''' or """

print(str1)

num1 = 1
num2 = 20
print(num1 + num2)

num3 = 2.1
num4 = 4.2
print(num3 + num4)
"""
컴퓨터는 이진수만 저장을 하게 되는데 소수는 정확라게 떨어지는 이진법으로 저장이 불가능하다
그래서 근사값을 저장하고 연산을 하게되면서 실제 값보다 아주 조금 더 크게 나온다.
"""
#boolean
"""
참과 거짓의 변수는 is 또는 has 또는 can등을 앞에 붙여주는게 좋다
부정은 보통 쓰지 않는다
"""
is_mz = True
is_empty = False
str5 = "python" #True
str6 = "" #False

#실습
#내 정보 출력해보기
print("제 이름은 " + last_name + first_name + "입니다")
print(age)
str7 = """만나서 반갑습니다"""
print(str7)
is_female = True

my_name = "김지원"
my_age = 21
my_height = 166
is_male = False
print("제 이름은 " + my_name)
print("제 나이는", my_age)
print("제 키는", my_height)
print("남자인가요? :", is_male)
print(f"제 이름은 {my_name}, 제 나이는 {my_age}, \n제 키는 {my_height}, 남자인가요?:{is_male}")

str8 = "\"안녕\t하세요\""
print(str8)

num5 = 10
num6 = 20
print(f"num1 + num2 = {num6 + num5}")