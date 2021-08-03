import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())

n_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse = True)

sum = 0
count = 1

for _ in range(m):
  if count > k:
    count = 1
    sum += n_list[1]

  else:
    count += 1
    sum += n_list[0]

print(sum)
