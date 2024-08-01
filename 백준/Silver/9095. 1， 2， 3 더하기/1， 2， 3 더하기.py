import sys
input = sys.stdin.readline

# 1 -> 1(1) 
# 2 -> 2(11,2)
# 3-> 4(12,21,111,3)
# 4 -> 7(1111,22,121,211,112,13,31)
# 5 -> 13
# (122,221,212,113,131,311,11111,14,41,23,32)
# 6 -> 24
# ==> dp(n) = dp(n-1)+dp(n-2)+dp(n-3)

t = int(input())
dp = [0]*12

dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7

answer = []

for i in range(5,12):
  dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for _ in range(t):
  n = int(input())
  answer.append(dp[n])

for i in answer:
  print(i)