N = int(input())
cnt = 0
l = [500, 100, 50, 10]
for i in l:
  cnt += N // i
  N %= i
print(cnt)