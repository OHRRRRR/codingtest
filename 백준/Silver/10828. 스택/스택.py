import sys
input = sys.stdin.readline

# 명령의 수 
n = int(input())

# 스택 정의
stack = []


# 명령 입력 받음
for _ in range(n):
  
  inputc = input().split()

  if inputc[0] == "push":
    stack.append(inputc[1])
    # print(stack)
  elif inputc[0] == "pop":
    if len(stack) != 0:
      print(stack.pop())
    else:
      print(-1)
  elif inputc[0] == "size":
    print(len(stack))
  elif inputc[0] == "empty":
    if len(stack) != 0:
      print(0)
    else:
      print(1)
  elif inputc[0] == "top":
    if len(stack) != 0:
      print(stack[len(stack)-1])
    else:
      print(-1)