# 게임 세팅 가져오기
from game_setting import game_setting

# 똥 가져오기

from func.make_dung import dung_list

# 똥맞았을 때, 참 거짓값 가져오기
from data.Game_State import Game_State

# gameover(똥이 닿았을 때, 실행)
from func.game_over import game_over



# 똥을 움직이게 해보자
# 0.5초마다 똥을 아래로 10만큼 움직이게 하기


def dung_down():
    # gameover되면 못움직이게 return 처리
    if Game_State.is_game_over:
        return
    # dung_list의 값들을 모두 가져온다.
    for dung_index,dung in enumerate(dung_list):      
      # 전역변수 dung_place를 가져옴
      dung.object_place.y += 10
      dung.place(x=dung.object_place.x, y=dung.object_place.y)
      # 만약에 dung의 y 좌표값이 800이상이라면?
      # 그 값을 제거하기(게임 최적화 목적)
      if(dung.object_place.y > 800):
        dung_list.pop(dung_index)
    # 만약에 is_game_over이 false면?(즉, 아직 게임오버가 안된 상황이면?)
    if not Game_State.is_game_over:
        # after 함수를 사용하여 0.5(50ms)초마다 재귀 동작을 하도록 함
        game_setting.after(50, dung_down)
        game_over()