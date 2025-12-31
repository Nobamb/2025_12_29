# 플레이어 가져오기
from data.player import player
# game_state의 is_game_over가 true면 동작 못하게 해보기
from data.Game_State import Game_State


# # 움직이게 지정
def move(event, value, object_place=player.object_place):
    # 만약에 game_over가 아닐 시,
    if not Game_State.is_game_over:
        # # 왼쪽으로 움직일 것이기에 player_x를 감소시킨다
        # global Object_place
        # 10만큼 감소
        object_place.x += value
        # 동작 테스트
        print("왼쪽이동", object_place.x)
        # 플레이어 위치 재설정
        return player.place(x=object_place.x, y=object_place.y)

