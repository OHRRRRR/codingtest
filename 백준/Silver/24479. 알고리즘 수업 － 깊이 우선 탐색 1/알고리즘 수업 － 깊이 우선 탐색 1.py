# 인접리스트로 구현함
# 출력은 i의 방문순서
# visited에 방문순서 저장 (cnt로 계산)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6) #파이썬으로 dfs 문제를 풀 때 무조건 사용

# 전역변수: global
# 지역변수: nonlocal

#정점, 간선 수, 시작정점
n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1) ] # 각 노드의 개수만큼 리스트 생성

visited = [0] * (n+1) # 방문순서 저장

for _ in range(m):
  u,v = map(int,input().split())
  graph[u].append(v) # 양방향 노드이므로 u-v, v-u 둘 다 연결됨
  graph[v].append(u)
  
cnt=1 # 아직 방문전이므로 1부터 시작

def dfs(v):
  global cnt
  visited[v] = cnt # 몇 번째 방문인지 저장 -> 방문순서 기록
  graph[v].sort() # 입력값을 정렬
  for i in graph[v]: # 인접 정점을 하나씩 방문
    if visited[i] == 0: # 아직 방문하지 않았다면
      cnt += 1 # 방문순서 +1 해주고
      dfs(i) # 재귀 호출해서 visited에 방문순서 기록

dfs(r)

for i in range(1,n+1):
  print(visited[i]) 
