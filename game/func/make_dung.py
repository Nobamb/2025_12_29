from game_setting import game_setting
from classFolder.Object import Object
from classFolder.Object_place import Object_place
from random import randint
from data.Game_State import Game_State

# 똥을 무한대로 만들어보자
# 똥 저장
dung_list = []

# 똥 생산 함수
def make_dung():
  # global로 지정
  global dung_list
  # 만약 is_game_over가 false일때?
  if not Game_State.is_game_over:
    # x값 범위
    x_range = randint(0,950)
    # 똥을 먼저 지정을 한다.
    new_dung = Object(game_setting,"💩", 1000, x_range, 0)
    # 똥에 대해 리스트를 추가한다.
    dung_list.append(new_dung)
    
    # 계속 생산하게 하기
    game_setting.after(50, make_dung)
    
  # 만약에 is_game_over값이 true면 
  # 생산을 중단한다.
  if Game_State.is_game_over:
    return