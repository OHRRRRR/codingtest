p =int(input())

for k in range(1,p+1):
    height_sort = []
    height = list(map(int, input().split()))
    ans = 0
    for i in range(1,len(height)):
        #제일 첫번째 값이라면 -> 삽입
        if i == 1:
            height_sort.append(height[i])
            continue
        #리스트 내에 있는 값 중 가장 큰 값일 경우 -> 맨뒤에 삽입
        now = height[i]
        if now > max(height_sort):
            height_sort.append(now)
            continue
        # 중간에 삽입되어야하는 경우-> 앞에서부터 탐색해서 현재 값보다 큰 값이 있다면 insert를 사용해서 그 인덱스에 삽입
        for j in range(len(height_sort)):
            if height_sort[j] > now:
                height_sort.insert(j, now)
                ans += (len(height_sort) - j - 1)
                break
    print(k,ans)