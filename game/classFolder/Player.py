# tk import
# 게임 기본 요소
import tkinter as tk
# Object_Place import
# 좌표설정
from classFolder.Object_place import Object_place
# 플레이어 클래스 지정

class Player:
  
  def __init__(self, game, text, size,place_x,place_y):
    # 요소 지정(적용할 게임, text, size)
    self.player = tk.Label(game, text=text, font=size)
    # 좌표값 설정
    self.player_place = Object_place(place_x, place_y)
    # 좌표값에 맞게 위치 지정
    self.player.place(x=self.player_place.x, y=self.player_place.y)


# # 요소를 움직이게 해보기
# player = tk.Label(game, text="😀", font=1000)


# # 플레이어의 x, y 좌표 설정
# player_place = Object_place(500, 700)


# # # 플레이어배치
# player.place(x=player_place.x, y=player_place.y)
