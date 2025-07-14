#Book 클래스
#제목과 저자 => title, author\
#display_info => "제목: [제목], 저자: [저자]"
#Book 클래스의 객체 두개 이상 만들어보고 display_info 호출
#소멸자 => 소멸 시 "[제목]의 객체가 소멸 되었습니다." 출력

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

    def dispaly_info(self):
        print(f"제목: [{self.title}], 저자: [{self.author}]")

    def __del__(self):
        print(f"[{self.title}]의 객체가 소멸 되었습니다.")

book1 = Book("채식주의자", "한강")
book1.dispaly_info()

book2 = Book("돈의 속성", "김승호")
book2.dispaly_info()