import sys
input = sys.stdin.readline

n = int(input()) # n은 1부터 1000까지

d = [0] * 1001

# 1과 2를 조합가지고 배열해서 만듦
# 1 - 2x1 1가지
# 2 - 2x2 2가지
# 3 - 2x3 3가지
# 4 - 2x4 5가지
# 5 - 2x5 8가지
# 6 - 2x6 13가지

d[1] = 1
d[2] = 2

for i in range(3,1001):
  d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n])