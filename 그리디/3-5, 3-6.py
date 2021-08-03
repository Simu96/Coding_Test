import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
count = 0

while(n != 1):
  if n % k == 0:
    n /= k
    count += 1
  else:
    n -= 1
    count +=1

print(count)

# k로 나누어 떨어지는 수로 n을 한번에 뺄셈할 수도 있다.
