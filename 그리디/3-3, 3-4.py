import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

num_list = [[0] * m for _ in range(n)]

for i in range(n):
  num_list[i] = list(map(int, sys.stdin.readline().rstrip().split()))


num_min_list = [0] * n

for i in range(n):
  num_min_list[i] = min(num_list[i])

print(max(num_min_list))
