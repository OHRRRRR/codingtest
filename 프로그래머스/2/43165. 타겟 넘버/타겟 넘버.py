def solution(numbers, target):
    answer = 0
    cal_result= [0]
    
    for num in numbers:
        cal_pm =[]
        for cal in cal_result:
            cal_pm.append(cal+num)
            cal_pm.append(cal-num)
        cal_result = cal_pm
        
    for i in cal_result:
        if i == target:
            answer+=1
            
    return answer