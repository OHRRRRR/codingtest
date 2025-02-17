import sys
input = sys.stdin.readline

n,p,q = map(int,input().split())

A = {}
A[0]=1

def solution(n):
    answer = 0
    if n in A:
        answer = A[n]
        return answer
    else:
        A[n]=solution(n//p)+solution(n//q)
        answer = A[n]
        return answer
        
print(solution(n))