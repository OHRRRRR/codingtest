import sys
input = sys.stdin.readline

# 출입 기록 수 n 
# 출입 기록 순서대로 주어짐
# 이름 -> 알파벳 대소문자로 구성된 5글자 이하의 문자열

n = int(input())
enter_list = {}
for _ in range(n):
  name, log = map(str,input().split())
  if log == "enter":
    enter_list[name] =True
  elif log == "leave":
     del enter_list[name]

sort_list = sorted(enter_list, reverse=True)

for i in sort_list:
  print(i)