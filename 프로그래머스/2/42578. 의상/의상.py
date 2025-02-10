def solution(clothes):
    answer = 0
    dict_clothes = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] in dict_clothes:
            dict_clothes[clothes[i][1]] += 1
        else:
            dict_clothes[clothes[i][1]] = 1
    
    if len(dict_clothes) == 1:
        answer = list(dict_clothes.values())[0]
    else:
        calc = 1
        for value in dict_clothes.values():
            calc *= (value + 1) 
        
        answer = calc - 1 
    
    return answer