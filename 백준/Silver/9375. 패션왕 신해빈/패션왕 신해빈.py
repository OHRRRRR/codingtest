import sys
input = sys.stdin.readline

n= int(input())
answer = 0
answer_list =[]
for _ in range(n):
    cnt = int(input())
    dict = {}
    for _ in range(cnt):
        wear, kind = map(str,input().split())
        if kind not in dict:
            dict[kind] = 1  
        else:
            dict[kind] += 1 

    if len(dict) == 1:
        answer = list(dict.values())[0]    
        answer_list.append(answer)
    else:
        calc=1
        for value in dict.values():
            calc *= (value+1)
            
        answer = calc - 1
        answer_list.append(answer)
       
for i in answer_list:
    print(i)