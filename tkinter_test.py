# tkinter import

import tkinter as tk

# 라이브러리 적용하는 것이 중요
root = tk.Tk()
print(root)


root.title("테스트 창")
root.geometry("400x300")


# 임의의 라벨 생성
label_test = tk.Label(root, text="테스트")
label_test.pack()



root.mainloop()