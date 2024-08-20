import sys
input = sys.stdin.readline

n = int(input())

# 5 -> (311)(11111)() SK
# 6 -> (33)(1111111)(1311) CY

if n%2==0: 
  print("CY")
else:
  print("SK")