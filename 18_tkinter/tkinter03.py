import tkinter as tk
from tkinter import messagebox

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
    #실제 서버와 데이터베이스에 정보를 요청해서
    #비교하는 중복확인 절차
    if id_entry.get() == "":
        messagebox.showwarning("경고", "아이디를 입력해주세요.")
    else:
        messagebox.showinfo("중복확인", "중복확인이 되었습니다.")


id_button = tk.Button(root, text="중복확인", command=chk_button_click)
id_button.grid(row=0, column=2)

password_label = tk.Label(root, text="비밀번호:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5)

chk_var = tk.IntVar()
chk_box = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_var)
chk_box.grid(row=3, column=1)

password_check = tk.Label(root, text="비밀번호 확인:")
password_check.grid(row=2, column=0)

password_check_entry = tk.Entry(root, show="*")
password_check_entry.grid(row=2, column=1)

def signup_click():
    if password_entry.get() != password_check_entry.get():
        messagebox.showerror("비밀번호 불일치"," 비밀번호가 일치하지 않습니다.")
    elif chk_var.get() == 0:
        messagebox.showwarning("약관동의 필요", "약관동의를 해주세요")
    elif chk_var.get() == 1 and password_entry.get() == password_check_entry.get():
        messagebox.showinfo("회원가입 완료", "회원가입이 완료되었습니다.")



signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=4, column=2)

root.mainloop()