import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    scores = list(map(int, input().rstrip().split()))
    counter = Counter(scores)
    board = {}
    tmp = 0
    for i in range(n):
        if counter[scores[i]] < 6:
            tmp += 1
            continue
        if scores[i] in board:
            board[scores[i]].append(i - tmp)
        else:
            board[scores[i]] = [i - tmp]
    print(sorted(board, key=lambda x:(sum(board[x][0:4]), board[x][4]))[0])