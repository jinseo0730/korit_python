import os
from package.models import Player
from package.utils import save_game, load_game
from package.constants import monsters
from package.game import battle, shop


def main():
    print("턴제 RPG 게임")
    if os.path.exists("save.json"):
        while True:
            choice = input("1. 기존 캐릭터 불러오기\n2. 새로 시작하기\n선택:")
            if choice == "1":
                # 플레이어 데이터 들고오기
                player = load_game()  # load_game에 대한 반환값이 player 객체
                if not player:
                    print("저장된 캐릭터가 없습니다.")
                    nickname = input("닉네임을 입력해 주세요 : ")
                    player = Player(nickname)
                break
            elif choice == "2":
                nickname = input("닉네임을 입력해 주세요 : ")
                player = Player(nickname)
                break
            else:
                print("잘못된 입력입니다.")
                continue
    else:
        nickname = input("닉네임을 입력해 주세요 : ")
        player = Player(nickname)

    while True:
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("메뉴 선택 : ")

        if choice == "1":
            print("\n[배틀]")
            #싸울 몬스터 선택
            for idx, monster in enumerate(monsters):
                print(f"{idx + 1}. {monster.name} (HP: {monster.hp}, 공격력: {monster.attack})")
            while True:
                try:
                    m_choice = int(input("몬스터를 선택하세요:")) - 1
                except ValueError:
                    print("잘못된 입력입니다.")
                    continue
                if 0 <= m_choice < len(monsters):
                    # 몬스터 배틀 시작
                    battle(player, monsters[m_choice])
                    break
                else:
                    print("잘못된 입력입니다.")
                    continue
        elif choice == "2":
            print("\n[상점]")
            #상점 함수
            shop(player)
        elif choice == "3":
            print("\n[내 아이템 확인]")
            if player.items:
                for item in player.items:
                    print(f"{item["name"]} (추가 공격력: {item["attack"]}, 추가 HP: {item["hp"]}, 추가 치명타 확률: {item["cri_luck"]}")
            else:
                print("보유한 아이템이 없습니다.")
        elif choice == "4":
            print("\n[내 정보 확인]")
            print(f"닉네임: {player.nickname}\n레벨: {player.level} ({player.exp}/{player.max_exp})\n공격력: {player.attack}\n치명타 확률: {player.cri_luck}%\nHP: {player.hp}\nMP: {player.mp}\n골드: {player.gold}")
        elif choice == "5":
            save_game(player)
            print("\n[게임 종료]")
            #게임을 저장하는 함수

            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()