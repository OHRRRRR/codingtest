import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
card = deque([])
c=0

for i in range(1,n+1):
  card.append(i)

while len(card)>1:
  for i in range(n-1):
    card.popleft()
    c= card.popleft()
    card.append(c)
print(card[0])