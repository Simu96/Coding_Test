import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

game_map = [[0] * m for _ in range(n)]

for a in range(n):
  # 문제 조건과 다르게 띄어쓰기로 split하여 입력 받음
  game_map[a] = list(map(int, sys.stdin.readline().rstrip().split()))

false = [[False] * m for _ in range(n)]

count = 0

def dfs(x, y):
  false[x][y] = True
  
  if x - 1 >= 0 and game_map[x-1][y] == 0 and false[x-1][y] == False:
    dfs(x-1, y)
  if x + 1 < n and game_map[x+1][y] == 0 and false[x+1][y] == False:
    dfs(x+1, y)
  if y - 1 >= 0 and game_map[x][y-1] == 0 and false[x][y-1] == False:
    dfs(x, y-1)
  if y + 1 < m and game_map[x][y+1] == 0 and false[x][y+1] == False:
    dfs(x, y+1)

for i in range(n):
  for j in range(m):
    if game_map[i][j] == 0 and false[i][j] == False:
      dfs(i, j)
      count += 1

print(count)
