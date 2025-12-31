# tkinter 가져오기
import tkinter as tk
# game_setting 가져오기
from game_setting import game_setting


# 끝내기 버튼
# game의 destroy 함수 지정(게임 끝내기)
finish_button = tk.Button(game_setting, text="끝내기",command=game_setting.destroy)
