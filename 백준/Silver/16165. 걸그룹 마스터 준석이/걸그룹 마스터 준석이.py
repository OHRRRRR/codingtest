import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
group_name = {}  
for i in range(n):
    name = input().rstrip()
    group_member = []  
    for u in range(int(input().rstrip())):
        member = input().rstrip()
        group_member.append(member)
    group_member.sort()
    group_name[name] = group_member

for i in range(m):
    quize = input().rstrip()
    if int(input().rstrip()) == 0:
        for m in group_name[quize]:
            print(m)
    else:
        for a in group_name.keys():
            if quize in group_name[a]:
                print(a)