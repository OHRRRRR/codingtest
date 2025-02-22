import sys
input = sys.stdin.readline

times = list(input().split())
start = int(times[0][:2]+times[0][3:])
end = int(times[1][:2]+times[1][3:])
quit = int(times[2][:2]+times[2][3:])

member = {}
count = 0
while True:
    chat = input()
    if len(chat) < 5:
        break
    
    c_time, name = map(str, chat.split())
    chat_time = int(c_time[:2] + c_time[3:])

    if chat_time <= start:
        member[name] = 1
    elif end <= chat_time <= quit and name in member:
        member[name] += 1

for key, value in member.items():
    if value >= 2:
        count += 1
        
print(count)