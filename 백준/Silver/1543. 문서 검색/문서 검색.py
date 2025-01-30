doc = input()
word = input()
length = len(word)
flag = [0 for i in range(len(doc))]

cnt = 0
for i in range(len(doc)):
    if flag[i] == 1:
        continue

    if word == doc[i:i+length]:
        cnt += 1
        for idx in range(i,i+length):
            flag[idx] = 1

print(cnt)