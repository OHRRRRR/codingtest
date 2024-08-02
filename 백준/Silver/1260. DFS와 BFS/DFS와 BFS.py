from collections import deque
import sys
input = sys.stdin.readline

#정점의 개수, 간성의 개수, 탐색 시작 정점 입력
n, m, v = map(int,input().split())

node = [[0]*(n+1) for _ in range(n+1)]

visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

for _ in range(m):
  a,b = map(int,input().split())
  node[a][b]=node[b][a]=1

# 깊이우선 탐색 -> 스택사용, 휴지곽
# 스택에 넣을 때 프린트해주면 됨
def dfs(v):
  visited_dfs[v] = 1
  print(v, end =" ")
  for i in range(1,n+1):
    if not visited_dfs[i] and node[v][i]==1:
      dfs(i)

#popleft로 가장 먼저 넣은 값부터 출력
def bfs(v):
  queue = deque([v])
  visited_bfs[v]=1

  while queue:
    v = queue.popleft()
    print(v, end=" ")

    for i in range(1,n+1):
      if not visited_bfs[i] and node[v][i]==1:
        visited_bfs[i]=1
        queue.append(i)



dfs(v)
print()
bfs(v)