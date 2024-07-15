import sys
input = sys.stdin.readline

# 카드의 개수
n = int(input().strip())

# 카드팩의 가격
card_input = list(map(int, input().strip().split()))

# DP 테이블 초기화
dp = [0] * (n + 1)

# DP로 최대값 계산
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + card_input[j - 1])

# 결과 출력
print(dp[n])