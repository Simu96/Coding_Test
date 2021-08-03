import sys

n = int(sys.stdin.readline().rstrip())
LRUD = list(map(str, sys.stdin.readline().rstrip().split()))

m = [1, 1]
for x in LRUD:
  if x == "L":
    if m[1] - 1 == 0:
      continue
    else:
      m[1] -= 1
  if x == "R":
    if m[1] + 1 == n + 1:
      continue
    else:
      m[1] += 1
  if x == "U":
    if m[0] - 1 == 0:
      continue
    else:
      m[0] -= 1
  if x == "D":
    if m[0] + 1 == n + 1:
      continue
    else:
      m[0] += 1

print(m[0], m[1])
