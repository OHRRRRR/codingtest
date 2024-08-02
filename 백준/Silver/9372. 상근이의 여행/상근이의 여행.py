import sys
input = sys.stdin.readline

def BFS(start):
  queue = [start]
  cnt = 0
  while queue:
    start = queue.pop(0)
    for i in range(1, n+1):
      if not visited[i] and airplane[start][i] == 1:
        queue.append(i)
        visited[i] = True
        cnt += 1
  return cnt

# 테스트케이스 종류
t = int(input())

for _ in range(t):
  # 국가의 수 n, 비행기의 종류 m
  n,m = map(int,input().split())
  airplane=[[0]*(n+1) for _ in range(n+1)]
  visited = [0] * (n+1)
  
  for _ in range(m):
    a,b = map(int,input().split())
    airplane[a][b]=1
    airplane[b][a]=1

  print(BFS(1)-1)