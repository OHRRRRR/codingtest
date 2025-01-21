import sys
input = sys.stdin.readline

stack = []
answer = [] 
temp = True
count = 1

n = int(input())

for i in range(n):
    num = int(input())

    while num >= count:
        answer.append("+")
        stack.append(count)
        count += 1
        
    if num == stack[-1]:
        answer.append("-")
        stack.pop()
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in answer:
        print(i)