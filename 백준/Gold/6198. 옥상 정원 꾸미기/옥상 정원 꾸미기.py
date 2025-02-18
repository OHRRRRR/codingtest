import sys
input = sys.stdin.readline

n = int(input().strip())  
height = []
for _ in range(n):  
    h = int(input().strip()) 
    height.append(h)

stack = []
cnt = 0

for h in height:
    while stack and stack[-1] <= h:  
        stack.pop()
    cnt += len(stack)  
    stack.append(h)  

print(cnt)