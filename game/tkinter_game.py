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

from classFolder.Player_place import Player_place

# 왼쪽으로 움직이게 하는 함수

from func.move_left import move_left

# 오른쪽으로 움직이게 하는 함수


game = tk.Tk()

game.title("똥피하기 게임")

game.geometry("1000x800")

# 요소를 움직이게 해보기
player = tk.Label(game, text="😀",font=1000)


# 플레이어의 x, y 좌표 설정
Player_place.x = 0
Player_place.y = 700



# # 왼쪽움직이게 지정
def move_left(event , Player_place=Player_place):
  # # 왼쪽으로 움직일 것이기에 player_x를 감소시킨다
  # global Player_place
  # 10만큼 감소
  Player_place.x -= 10
  # 동작 테스트
  print("왼쪽이동",Player_place.x)
  # 플레이어 위치 재설정
  return player.place(x=Player_place.x, y=Player_place.y)


# # 오른쪽움직이게 지정
def move_right(event, player_place=Player_place):
  # # 오른쪽으로 움직일 것이기에 player_x를 증가시킨다
  # global Player_place
  # 10만큼 증가
  Player_place.x += 10
  # 동작 테스트
  print("오른쪽 이동",Player_place.x)
  # 플레이어 위치 재설정
  return player.place(x=Player_place.x, y=Player_place.y)




# 왼쪽 키를 누르면 왼쪽으로 이동
player.bind("<Left>",move_left)
# 오른쪽 키를 누르면 오른쪽으로 이동
player.bind("<Right>",move_right)
# 포커스 설정(키 입력을 받기 위해서 필요)
player.focus_set()




# # 플레이어배치
player.place(x=Player_place.x, y=Player_place.y)

game.mainloop()


