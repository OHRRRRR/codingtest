def solution(numbers, target):
    answer = 0
    leaves = [0] # 모든 계산 결과 담기게 함
    for num in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)
        leaves = tmp
    for i in leaves:
        if i == target:
            answer+=1
    return answer


