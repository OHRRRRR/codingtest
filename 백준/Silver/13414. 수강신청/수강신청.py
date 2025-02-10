import sys
input = sys.stdin.readline

n,m = map(int, input().split())
students = {}
for _ in range(m):
    student = input().rstrip()
    if student in students:
        students.pop(student)
    students[student] = 1

print(*list(students.keys())[:n], sep="\n")
