import sys
input = sys.stdin.readline

#굴다리의 길이 n
n = int(input())
#가로등의 개수 m
m = int(input())
#각 가로등의 위치 x들
x = list(map(int,input().split()))

answer_list = []
answer=0

if len(x) == 1:
  answer_list.append(x[0])
  answer_list.append(n-x[0])
else:
  answer_list.append(x[0])
  for i in range(1,len(x)):
    answer_list.append(int((x[i] - x[i - 1]) / 2 + 0.5))  # 정확한 중간값 계산 후 반올림
  answer_list.append(n-x[len(x)-1])
  

# print(answer_list)
print(max(answer_list))
