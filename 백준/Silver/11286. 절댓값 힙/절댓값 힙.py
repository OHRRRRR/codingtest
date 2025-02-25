import sys
import heapq

input = sys.stdin.readline

n = int(input())
array_plus = [] 
array_minus = [] 

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(array_plus, x)  
    elif x < 0:
        heapq.heappush(array_minus, -x) 
    else:
        if not array_minus and not array_plus:
            print(0)
        elif array_minus and (not array_plus or array_minus[0] <= array_plus[0]):
            print(-heapq.heappop(array_minus))  
        else:
            print(heapq.heappop(array_plus))  