# 오브젝트 가져오기
from data.player import player
from func.make_dung import dung_list
# dung_bool 가져오기
from data.Game_State import Game_State
# 버튼 가져오기
from game_over_button.finish_button import finish_button
from game_over_button.re_button import re_button


# 똥이 내려왔을 때(어느정도 거리값 제공), 닿으면 게임오버하는 기믹 생성
# 닿았을 때, 게임오버와 동시에 다시 실행 및 나가기 버튼 생김
# 다시 실행 클릭시, 처음부터 다시
# 나가기 버튼 클릭시, 바로 끝냄


def game_over():
    # dung_bool 가져오기
    global Game_State
    # 모든 dung에 대해 지정
    for dung in dung_list:    
      if (
          player.object_place.y <= dung.object_place.y + 20 and player.object_place.y >= dung.object_place.y - 20
      ) and (player.object_place.x <= dung.object_place.x + 20 and player.object_place.x >= dung.object_place.x - 20):
          print("게임 오버")
          # is_game_over true값 변경
          Game_State.is_game_over = True
          # 다시하기 버튼 생성
          re_button.pack()
          # 끝내기 버튼 생성
          finish_button.pack()  
