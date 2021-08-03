import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
x, y, dir = list(map(int, sys.stdin.readline().rstrip().split()))
game_map = [[0] * m for _ in range(n)]
for j in range(n):
  game_map[j] = list(map(int, sys.stdin.readline().rstrip().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 처음 시작 위치는 무조건 count
count = 1

def check(x, y, dir):
  if game_map[x+dx[dir]][y+dy[dir]] == 0:
    return True
  else:
    return False

def turn_left(dir_x):
  if dir_x == 0:
    return 3
  else:
    return dir_x - 1


# 네 방향 모두 검사했는지를 판단하는 변수
false = 0

while(True):
  if check(x, y, turn_left(dir)):
    false = 0
    game_map[x][y] = 1
    x += dx[turn_left(dir)]
    y += dy[turn_left(dir)]
    dir = turn_left(dir)
    count += 1
  else:
    false += 1
    dir = turn_left(dir)
    # 네 방향 모두 갈 수 없는 경우
    if false == 4:
      if dir > 1:
        back = dir - 2
      else:
        back = dir + 2

      if game_map[x+dx[back]][y+dy[back]] == 1: # 더이상 뒤로 갈 수 없는 경우
        break
      else:
        game_map[x][y] = 1
        x += dx[back]
        y += dy[back]
    
print(count)
