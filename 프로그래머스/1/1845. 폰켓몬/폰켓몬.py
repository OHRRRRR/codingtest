def solution(nums):
    answer = 0
    list = []
    N = (len(nums))/2
    for i in nums:
        if i in list:
            pass
        else:
            list.append(i)

    if len(list) >= N:
        answer = N
    else:
        answer = len(list)

    return answer
