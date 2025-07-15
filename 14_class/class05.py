#Account 클래스 => 계좌 정보
#owner 그리고 balance => 잔액은 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
#withdraw 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
#만약에 잔액이 부족하다면 출금을 할 수 없도록 출력

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}님의 계좌가 개설되었습니다. 잔액: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.\n잔액: {self.balance}원")
        else:
            print("입금액은 0보다 커야 합니다.")

    def withdraw(self, amount):
        if amount <= 0: #출금액이 0보다 작은 상황
            print("출금액은 0보다 커야 합니다.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.\n잔액: {self.balance}원")
        else: #출금액이 0이상이면서 잔액보다 출금액이 더 많은 상황
            print(f"잔액이 부족합니다. 현재 잔액: {self.balance}")

person1 = Account("gildong", 10000)
person1.deposit(20000)
person1.withdraw(15000)
person1.withdraw(20000)
person1.withdraw(-1000)







