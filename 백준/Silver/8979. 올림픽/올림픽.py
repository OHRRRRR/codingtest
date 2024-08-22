import sys
input = sys.stdin.readline

#국가의 수, 등수를 알고 싶은 국가
n,k = map(int,input().split())


medal_list=[]

for i in range(n):
  nation,g,s,b = map(int,input().split())
  medal_list.append((g,s,b)) #메달만 medal_list배열에 추가

# 등수 알고 싶은 국가의 메달 수 저장

  if nation == k:
    find_medal = (g,s,b)

#메달 내림차순 정렬
medal_list.sort(reverse=True)

for i in range(n):
  if find_medal==medal_list[i]:
    print(i+1)
    break