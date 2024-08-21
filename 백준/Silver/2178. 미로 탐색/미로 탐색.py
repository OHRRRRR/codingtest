
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

graph = [[0]*(m) for _ in range(n)]

for i in range(n):
  graph[i] = list(map(int,input().rstrip()))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

def bfs(x, y):
  q = deque([(x,y)])

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
			
            # if문 하나에서 여러 조건을 확인하는 것 보다 아래처럼 쪼개는 것이 속도가 빠름
      if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1: 
        q.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1
  
bfs(0,0)  
print(graph[n-1][m-1])
    