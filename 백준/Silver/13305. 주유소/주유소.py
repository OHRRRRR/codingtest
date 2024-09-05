# 도시의 개수
n = int(input())
# 두 도시를 연결하는 도로의 길이
load_length = list(map(int,input().split()))
# 주유소의 리터당 가격
cost = list(map(int,input().split()))

answer = 0
answer_list = []

# 뒤의 리터당 가격보다 크면
  # 딱 갈 수 있는 만큼만 간 비용 정답에 더함
# 뒤의 리터당 가격보다 작으면
  # 딱 갈 수 있는 만큼만 간 비용 정답에 더함
  # 끝까지 간 비용 정답리스트에 추가
# 같으면 
  # 딱 갈 수 있는 만큼만 간 비용 정답에 더함

for i in range(n-1):
  # print(i,"i")
  summ = 0
  if i == n-1:
    answer_list.append(answer)
    # print(answer_list, " 1")
    
  if cost[i]>cost[i+1]:
    answer += cost[i] * load_length[i]
    # print(answer," 2")

  if cost[i]<cost[i+1]:
    for k in range(i, n-1):
      summ += load_length[k] 
      # print(summ," summ")
    answer_list.append(answer+cost[i]*summ)
    # print(answer_list, " 3")
    
    answer += cost[i] * load_length[i]
    # print(answer,"4")
    
  if cost[i]==cost[i+1]:
    answer += cost[i] * load_length[i]
    # print(answer," 5")
    # print(i,"i2")
    if i == n-2:
      answer_list.append(answer)

    
print(min(answer_list))