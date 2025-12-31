from player import player

# # 움직이게 지정
def move(event, value, object_place=player.object_place):
    # # 왼쪽으로 움직일 것이기에 player_x를 감소시킨다
    # global Object_place
    # 10만큼 감소
    object_place.x += value
    # 동작 테스트
    print("왼쪽이동", object_place.x)
    # 플레이어 위치 재설정
    return player.place(x=object_place.x, y=object_place.y)

