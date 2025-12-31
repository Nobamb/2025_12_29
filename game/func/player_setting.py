# player 가져옴
from data.player import player 
# move 가져옴
from func.move import move

# 플레이어 관련 세팅
def player_setting():
  # 왼쪽 키를 누르면 왼쪽으로 이동
  # 람다함수 사용하여 event(대표 파라미터)를 던져서 event, -10을 적용
  player.bind("<Left>", lambda event:move(event, -10))
  # 오른쪽 키를 누르면 오른쪽으로 이동
  player.bind("<Right>", lambda event:move(event, +10))
  # 포커스 설정(키 입력을 받기 위해서 필요)
  player.focus_set()
