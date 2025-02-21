def solution(s):
    right = 0  
    left = 0   

    for i in range(len(s)):
        if i == 0 and s[i] == ')':  
            return False
        
    for char in s:
        if right > left:  
            return False
        
        if char == '(':
            left += 1
        else:
            right += 1

    return left == right 