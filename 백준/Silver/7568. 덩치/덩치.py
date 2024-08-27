import sys
input = sys.stdin.readline

n = int(input())

dungchi=[]

answer = []

for _ in range(n):
  x,y = map(int,input().split())
  dungchi.append((x,y))


for i in range(n):
  cnt=0
  for j in range(n):
    # 등수 = 자기보다 큰 사람의 수 + 1 -> cnt + 1
    if dungchi[i][0]<dungchi[j][0] and dungchi[i][1]<dungchi[j][1]:
      cnt+=1
  answer.append(cnt+1)

for d in answer:
  print(d, end=" ")
