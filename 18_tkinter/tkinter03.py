import tkinter as tk

root = tk.Tk()
root.title("회원가입")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

#entry 옆에 버튼 하나 만들고 해당 버튼 클릭시
#아이디 출력
#아이디 밑에 비밀번호도 똑같이 만드세요
def chk_button_click():
    print(id_entry.get())
    print(password_entry.get())


id_button = tk.Button(root, text="확인", command=chk_button_click)
id_button.grid(row=0, column=2, padx=10)

password_label = tk.Label(root, text="비밀번호:")
password_label.grid(row=1, column=0, pady=10)

password_entry = tk.Entry(root)
password_entry.grid(row=1, column=1, padx=5)


root.mainloop()