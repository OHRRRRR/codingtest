import sys 
input = sys.stdin.readline

# 테스트 케이스 개수 입력 받음
t = int(input())

# 입력 받는 값이 1000000보다 작거나 같기 때문
# d = 입력받은 값이 인덱스 번호라고 했을 때의 각 방법의 수를 저장
d = [0] * 1000001

# 4전까지는 규칙이 적용되지않기 때문에 3까지 미리 값 넣어둠
d[1] = 1
d[2] = 2
d[3] = 4

# 방법의 수를 1000000009로 나눈 나머지를 출력하는 것이므로
for i in range(4, 1000001):
  d[i] = ( d[i-1] + d[i-2] +d[i-3] ) % 1000000009

# 정답을 저장할 배열
answer = []

# n 입력받기
for _ in range(t):
  n = int(input())
  answer.append(d[n])

for i in answer:
  print(i)