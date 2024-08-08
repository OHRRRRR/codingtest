# 지렁이는 인접한 다른 배추로 이동 가능
# (상하좌우 네방향)
# 0-> 배추 없음, 1-> 배추 있음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 지렁이 움직일 수 있는 범위
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<m and 0<=ny<n:
      if graph[ny][nx]==1:
        graph[ny][nx]=0
        dfs(nx,ny)
      
# 테스트케이스 개수
t = int(input())

# 배추를 심은 배추밭의 가로길이m, 세로길이n, 배추가 심어져 있는 위치의 개수=k
for _ in range(t):
  m,n,k = map(int,input().split())
  # 배추밭
  graph = [[0]* (m) for _ in range(n)]
  count = 0
    
  for _ in range(k):
    x,y = map(int,input().split())
    graph[y][x]=1
  for x in range(m):
    for y in range(n):
      if graph[y][x]==1:
        dfs(x,y)
        count+=1
  print(count)