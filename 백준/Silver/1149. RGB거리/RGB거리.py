# 집은 빨강,초록,파랑 중 하나의 색으로 칠함

# 1번 집의 색은 2번 집의 색과 같지 않아야함
# n번 집의 색은 n-1번 집의 색과 같지 않아야 함
# i번 집의 색은 i-1번 집의 색과 같지 않아야 함

# dp[n]은 모든 집을 칠하는 비용의 최소값

# 1번 집 -> 빨 
# 2, 3번 집 -> 초 파 or 파 초



n = int(input())

#집을 칠하는 비용 저장
house = [[0]*3 for _ in range(n)]

for i in range(n):
  house[i] = list(map(int,input().split()))

for i in range(1,n):
  #빨
  house[i][0] = min(house[i-1][1],house[i-1][2]) + house[i][0]
  #초
  house[i][1] = min(house[i-1][0],house[i-1][2]) + house[i][1]
  #파
  house[i][2] = min(house[i-1][0],house[i-1][1]) + house[i][2]


print(min(house[n-1]))
  