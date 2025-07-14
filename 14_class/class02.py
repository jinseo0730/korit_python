import time

class Player: #클래스명은 대문자로 시작해야됨
    def __init__(self, nickname, hp=100, gold=0, level=1):
        #nickname은 필수값, 나머지는 기본값이 정의되어 있다.
        self.nickname = nickname
        self.hp = hp
        self.gold = gold
        self.level = level
        print(f"닉네임 : {self.nickname}\nHP : {self.hp}\nGOLD : {self.gold}\nLEVEL : {self.level}")

    def __del__(self):
        print("저장중...")
        print("저잗되었습니다!")

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname
        print(f"{self.nickname}으로 닉변되었습니다.")
        #현재 객체의 nickname 속성을 새로운 닉네임으로 변경

player1 = Player("모험가")
player1.change_nickname("모험가2")
print("player의 현재 닉네임:", player1.nickname)