import tkinter as tk

# Game 클래스 지정
class Game:
  def __init__(self,width, height, title, geometry):
    # tk가져오기(게임 시작)
    self.game = tk.Tk()

    # 사이즈조절 가능 여부 설정
    # 둘다 조절 못하게 설정
    self.game.resizable(width, height)


    # 제목 똥피하기 게임
    # 크기 1000(가로) 800(세로)
    self.game.title(title)

    self.game.geometry(geometry)
