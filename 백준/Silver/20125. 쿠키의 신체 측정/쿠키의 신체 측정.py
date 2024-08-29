n = int(input())

cookie = [[]*(n) for _ in range(n)]

for i in range(n):
  cookie[i] = input()

heart_x = 0
heart_y = 0
body = []
cnt = 0

# 심장찾기
for i in range(n-1):
  for j in range(n-1):
    if i>0 and j>0:
      if cookie[i+1][j]=="*" and cookie[i][j+1]=="*" and cookie[i-1][j]=="*" and cookie[i][j-1]=="*":
        heart_x=i+1
        heart_y=j+1

#왼쪽 팔 찾기
for i in range(heart_y-1):
  if cookie[heart_x-1][i]=="*":
    cnt+=1
body.append(cnt)
cnt=0

#오른쪽 팔 찾기
for i in range(heart_y,len(cookie)):
  if cookie[heart_x-1][i]=="*":
    cnt+=1
body.append(cnt)
cnt=0

#허리 찾기
for i in range(heart_x,n):
  if cookie[i][heart_y-1]=="*":
    cnt+=1
body.append(cnt)
cnt=0

#왼쪽다리 찾기
for i in range(heart_x-1+body[2],n):
  if cookie[i][heart_y-2]=="*":
    cnt+=1
body.append(cnt)
cnt=0

#오른쪽다리 찾기
for i in range(heart_x-1+body[2],n):
  if cookie[i][heart_y]=="*":
    cnt+=1
body.append(cnt)

print(heart_x, end=" ")
print(heart_y)
for i in range(5):
  print(body[i], end = " ")