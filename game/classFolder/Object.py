# tk import
# 게임 기본 요소
import tkinter as tk
# Object_Place import
# 좌표설정
from classFolder.Object_place import Object_place

# 플레이어 클래스 지정
class Object(tk.Label):
  
  def __init__(self, game, text, size,place_x,place_y):
    # tk.Label 상속
    super().__init__(game, text=text, font=size)
    # 좌표값 설정
    self.object_place = Object_place(place_x, place_y)
    # 좌표값에 맞게 위치 지정
    self.place(x=self.object_place.x, y=self.object_place.y)


# # 요소를 움직이게 해보기
# player = tk.Label(game, text="😀", font=1000)


# # 플레이어의 x, y 좌표 설정
# player_place = Object_place(500, 700)


# # # 플레이어배치
# player.place(x=player_place.x, y=player_place.y)
