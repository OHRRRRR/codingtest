import sys
input = sys.stdin.readline
 
dict = {} 
cnt = 0
list = []
answer = 0

s = input().strip()
list.extend(s)

for i in range(len(s)):
    for j in range(i+1, len(s)+1):  
        dict[cnt] = s[i:j]  
        cnt += 1


answer += len(set(dict.values()))



print(answer)