import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

game_map = [[0] * m for _ in range(n)]

for a in range(n):
  # 문제 조건과 다르게 띄어쓰기로 split하여 입력 받음
  game_map[a] = list(map(int, sys.stdin.readline().rstrip().split()))

def bfs(x, y):
  queue = deque([(x, y)])
  
  while queue:
    x, y = queue.popleft()

    if x - 1 >= 0 and game_map[x-1][y] == 1:
      game_map[x-1][y] = game_map[x][y] + 1
      queue.append((x-1, y))
    if x + 1 < n and game_map[x+1][y] == 1:
      game_map[x+1][y] = game_map[x][y] + 1
      queue.append((x+1, y))
    if y - 1 >= 0 and game_map[x][y-1] == 1:
      game_map[x][y-1] = game_map[x][y] + 1
      queue.append((x, y-1))
    if y + 1 < m and game_map[x][y+1] == 1:
      game_map[x][y+1] = game_map[x][y] + 1
      queue.append((x, y+1))
  
  return game_map[n-1][m-1]

print(bfs(0, 0))
