#연결요소 개수 구하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v):
  visited[v]=1

  for node in graph[v]:
    if not visited[node]:
      dfs(node)

# 정점의 개수, 간선의 개수
n,m = map(int,input().split())

# 방향없는 그래프
graph = [[] for _ in range(n+1)]

# 방문기록 저장
visited = [0]*(n+1)

# 간선의 양끝점
for _ in range(m):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

cnt = 0
for i in range(1,n+1):
  if not visited[i]:
    dfs(i)
    cnt+=1

print(cnt)
    
    