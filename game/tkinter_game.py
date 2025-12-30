# tkinter 불러오기

# 1. tkinter를 사용하여 똥피하기 게임 만들어보기
# 2. 사람을 움직일 수 있게 만들어보기 v
# 3. 똥을 맞을 시에 게임오버되게
# 4. 점수기능 넣기
# 5. 똥이 점점 빨라지게 만들어보기
# 6. 똥이 랜덤한 위치에서 나오게 만들어보기
# ===========================================
# 6번까지 만들었을 때 기능 넣어보기
# 7. 똥을 피할 때 마다 일정 확률로 재화 획득
# 8. 아이템 기능 넣기(똥 맞기 1회 방지, 3초 무적, 똥 느리게 등)
# 9. 상점 기능 추가
# 10. 게임 기록 저장


import tkinter as tk

# 게임 관련 클래스(가져오기)

from classFolder.Object_place import Object_place

game = tk.Tk()

game.title("똥피하기 게임")

game.geometry("1000x800")


# 요소 ========================================================================

# 요소를 움직이게 해보기
player = tk.Label(game, text="😀", font=1000)


# 플레이어의 x, y 좌표 설정
player_place = Object_place(500, 700)


# # 플레이어배치
player.place(x=player_place.x, y=player_place.y)

# 똥내려오게 하기
# 똥 생성
dung = tk.Label(game, text="💩", font=1000)

# 똥의 초기 위치 지정
dung_place = Object_place(400, 200)

# 똥 위치 지정
dung.place(x=dung_place.x, y=dung_place.y)



# 움직임 관련=====================================================




# # 왼쪽움직이게 지정
def move_left(event, player_place=player_place):
    # # 왼쪽으로 움직일 것이기에 player_x를 감소시킨다
    # global Object_place
    # 10만큼 감소
    player_place.x -= 10
    # 동작 테스트
    print("왼쪽이동", player_place.x)
    # 플레이어 위치 재설정
    return player.place(x=player_place.x, y=player_place.y)


# # 오른쪽움직이게 지정
def move_right(event, player_place=player_place):
    # # 오른쪽으로 움직일 것이기에 player_x를 증가시킨다
    # global Object_place
    # 10만큼 증가
    player_place.x += 10
    # 동작 테스트
    print("오른쪽 이동", player_place.x)
    # 플레이어 위치 재설정
    return player.place(x=player_place.x, y=player_place.y)


# 왼쪽 키를 누르면 왼쪽으로 이동
player.bind("<Left>", move_left)
# 오른쪽 키를 누르면 오른쪽으로 이동
player.bind("<Right>", move_right)
# 포커스 설정(키 입력을 받기 위해서 필요)
player.focus_set()


# 다시하기 버튼

re_button = tk.Button(game, text="다시하기")


# 끝내기 버튼
# game의 destroy 함수 지정(게임 끝내기)
finish_button = tk.Button(game, text="끝내기",command=game.destroy)


# dung_bool
# 똥이 더이상 내려올 지에 대한 조건 값
# 기본값은 false
# game_over에서 일정 범위내에 들어왔을 때
# true로 변환을 하기(똥 멈추게)
dung_bool = False



# 똥이 내려왔을 때(어느정도 거리값 제공), 닿으면 게임오버하는 기믹 생성
# 닿았을 때, 게임오버와 동시에 다시 실행 및 나가기 버튼 생김
# 다시 실행 클릭시, 처음부터 다시
# 나가기 버튼 클릭시, 바로 끝냄


def game_over():
    # dung_bool 가져오기
    global dung_bool
    if (
        player_place.y <= dung_place.y + 10 and player_place.y >= dung_place.y - 10
    ) and (player_place.x <= dung_place.x + 10 and player_place.x >= dung_place.x - 10):
        print("게임 오버")
        # dung_bool true값 변경
        dung_bool = True
        # 다시하기 버튼 생성
        re_button.pack()
        # 끝내기 버튼 생성
        finish_button.pack()  


# 똥을 움직이게 해보자
# 0.5초마다 똥을 아래로 10만큼 움직이게 하기


def dung_down():
    # gameover되면 못움직이게 return 처리
    if dung_bool:
        return
    # 전역변수 dung_place를 가져옴
    global dung_place
    dung_place.y += 10
    dung.place(x=dung_place.x, y=dung_place.y)
    # 만약에 dung_bool이 false면?(즉, 아직 게임오버가 안된 상황이면?)
    if not dung_bool:
        # after 함수를 사용하여 0.5(50ms)초마다 재귀 동작을 하도록 함
        game.after(50, dung_down)
        game_over()









# 게임 시작 ==========================================================================

# 바로 똥 내려오게 실행

dung_down()
# 게임 실행
game.mainloop()
