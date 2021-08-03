import sys

m = list(sys.stdin.readline().rstrip())
count = 0
col_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = int(m[1]) - 1
col = m.index(m[0])

if col + 2 < 8:
  if row - 1 >= 0:
    count +=1
  if row + 1 < 8:
    count +=1

if col - 2 >= 0:
  if row - 1 >= 0:
    count +=1
  if row + 1 < 8:
    count +=1

if row + 2 < 8:
  if col - 1 >= 0:
    count +=1
  if col + 1 < 8:
    count +=1

if row - 2 >= 0:
  if col - 1 >= 0:
    count +=1
  if col + 1 < 8:
    count +=1

print(count)
