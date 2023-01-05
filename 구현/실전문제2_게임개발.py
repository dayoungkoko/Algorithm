n, m = map(int, input().split())
a, b, direction = map(int, input().split())
lst = [[] * i for i in range(n)]
for i in range(n):
    lst[i] = list(map(int, input().split()))

d = [[0] * m for _ in range(n)]
d[a][b] = 1

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


cnt = 1
turn_time = 0
while True:
    turn_left()
    dx = a + dir[direction][0]
    dy = b + dir[direction][1]
    if d[dx][dy] == 0 and lst[dx][dy] == 0:
        d[dx][dy] = 1
        a = dx
        b = dy
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        dx = a - dir[direction][0]
        dy = b - dir[direction][1]
        if lst[dx][dy] == 0:
            a = dx
            b = dy
        else:
            break
        turn_time = 0
print(cnt)