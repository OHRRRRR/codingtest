import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict = {}
answer = []
for _ in range(n):
    site, password = map(str,input().split())
    dict[site]=password
    
for _ in range(m):
    q = input().rstrip()
    answer.append(dict[q])
    
for i in answer:
    print(i)