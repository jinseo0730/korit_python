#Account 클래스 => 계좌 정보
#owner 그리고 balance => 잔액은 생성될 때 0으로 초기화
#deposit 메소드를 추가하여 잔액을 증가 시키고 증가된 잔액을 출력
#withdraw 메소드를 추가하여 잔액을 감소 시키고 감소된 잔액을 출력
#만약에 잔액이 부족하다면 출금을 할 수 없도록 출력

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_money):
        if deposit_money <= 0:
            print("양수를 입력해주세요")
        else:
            print(f"{deposit_money}원이 입금되었습니다.\n잔액: {self.balance + deposit_money}원")

    def withdraw(self, withdraw_money):
        if withdraw_money <= 0:
            print("양수를 입력해주세요")
        elif withdraw_money > self.balance:
            print("잔액이 부족합니다.")
        else:
            print(f"{withdraw_money}원이 출금되었습니다.\n잔액: {self.balance - withdraw_money}원")

person1 = Account("gildong", 10000)
person1.withdraw(1000)







