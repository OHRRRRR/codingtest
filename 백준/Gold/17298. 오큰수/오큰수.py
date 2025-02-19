import sys
input = sys.stdin.readline

n = int(input().strip())  
nums = list(map(int, input().strip().split()))
answer = [-1] * n  
stack = [] 
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        index = stack.pop()
        answer[index] = nums[i] 
    stack.append(i)  
    
print(*answer)