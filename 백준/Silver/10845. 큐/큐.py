import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([])
for _ in range(n):
    command=[]
    command = list(map(str,input().split()))
    
    if command[0] == "push":
        q.append(command[1])
        
    elif command[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q[0])
            q.popleft()
            
    elif command[0] == "size":
        print(len(q))
            
    elif command[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
        
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[len(q)-1])
    
