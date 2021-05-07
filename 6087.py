from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
sx = sy = ex = ey = -1
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j
q.append((sx, sy))
dist[sx][sy] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        while 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '*':
                break
            if dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
            nx += dx[k]
            ny += dy[k]
print(dist[ex][ey]-1)
