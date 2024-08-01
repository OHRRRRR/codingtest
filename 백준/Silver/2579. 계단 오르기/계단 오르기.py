# 계단 
# 1의배수->10
# 2의배수->20
# 3의배수->15
# 4의배수->25 -> 부터시작 반복 

# 한번에 한계단 또는 두계단 오를 수 있음
# 연속 3개단 밟기 불가
# 마지막 도착계단은 반드시 밟기
# -> 이걸 지켰을 때 게임에서 얻을 수 있는 점수 최댓값 구하기

# 1.일반적인 생각 = 어디로 올라갈까? -> 연속해서 계단을 몇 개 밟았는지 알아야함

# 2. 문제를 쉽게 해결하기 위한 생각 = 어디에서 올라왔을까? (한칸전인지 두칸전인지만 생각해주면 됨)
# dp(n): n까지 올라왔을 때 얻을 수 있는 최대값
# dp(n): max(직전칸에서 올라온 경우의 최대값, 전전칸에서 올라온 경우의 최대값)
# = max(stairs[n]+stairs[n-1]+dp(n-3)
#      , stairs[n]+dp(n-2))


import sys
input = sys.stdin.readline

# 계단점수
stairs= [0] * 301


#계단의 개수 입력
n = int(input()) # n은 300이하의 자연수
for i in range(1,n+1):
  stairs[i] = int(input())

#dp[n] = 계단 n을 오르는 경우의 수의 최대값
dp = [0] * 301

dp[1]=stairs[1]
dp[2]=stairs[1]+stairs[2]
dp[3]=max(stairs[1]+stairs[3],stairs[2]+stairs[3])
dp[4]=max(stairs[1]+stairs[2]+stairs[4],stairs[1]+stairs[3]+stairs[4])
for i in range(5,n+1):
  dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3],stairs[i]+dp[i-2])

print(dp[n])