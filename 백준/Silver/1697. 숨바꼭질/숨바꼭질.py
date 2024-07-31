# 수빈위치: n, 동생위치: k
# 수빈 걷는다면 ->  x-1 or x+1
# 수빈 순간이동 -> 2*x
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

# 방문위치를 표시하기 위한 방법을 생각해 visited 하나 만듦

# 수빈이가 갈수 있는 경우의 수 다 저장하고 
# 그 중에 가장 최소값 출력
  
import sys
input = sys.stdin.readline
from collections import deque


def bfs():
  q = deque()
  q.append(n)
  while q:
    v =  q.popleft() # v는 q의 leftpop값
    if v==k: # 만약 v가 k와 같다면 
      print(visited[v])
      break
    for next_v in (v-1, v+1, 2*v):
      if 0 <= next_v <MAX and not visited[next_v]:
      #만약 v-l,v+1, 2*v의 값이 범위 내에 있고, 방문하지않았다면
        visited[next_v] = visited[v] + 1
        q.append(next_v)

MAX = 1000001 # 시간초과를 막기 위한 수 제한
visited = [0] * (MAX+1) # 이동하는 거리를 알기위한 변수

n,k = map(int,input().split())

bfs()