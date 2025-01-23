# 높이 n 왼->오
# 송신기는 수평직선의 횐쪽 방향으로 발사
# ex) 높이가 6,9,5,7,4 수평 직선에 일렬, 모든 탑에서 왼쪽으로 동시에 레이저 발사
# 높이 4인 탑에서 발사한 레이저 신호 -> 높이7 탑이 수신
# 높이 7 -> 높이 9
# 높이 5 -> 높이 9
# 높이 9,6 -> 어떤 탑에서도 수신하지 못함
# 각각의 탑에서 발사한 레이저 신호 어느 탑에서 수신하는지 알아내는 문제

import sys
input = sys.stdin.readline

n = int(input())

tower = list(map(int,input().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] >= tower[i]: # 수신할 탑 존재
            result.append(stack[-1][0]+1) # 인덱스 값 + 1 해줘야 수신할 탑의 번호가 됨
            break
        else: stack.pop()

    if not stack:
        result.append(0) # 스택이 비어있으면 수신할 탑이 없으므로 0

    stack.append((i, tower[i])) # 탑의 인덱스와 높이는 일단 stack에 집어 넣어야 함 

for i in result:
    print(i, end = ' ')

