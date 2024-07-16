import sys 
input = sys.stdin.readline

n = int(input())

answer = 0

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse = True)

for i in range(n):
  answer += a[i] * b[i]

print(answer)