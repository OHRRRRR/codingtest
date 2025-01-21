import sys
input= sys.stdin.readline

k = int(input())
stack = []
for i in range(k):
    jungsu = int(input())
    if jungsu == 0:
        stack.pop()
    else:
        stack.append(jungsu)
        
print(sum(stack))