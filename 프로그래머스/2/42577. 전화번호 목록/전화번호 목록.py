def solution(phone_book):
    answer = True
    phone = {}
    cnt = 0
    
    for i in range(len(phone_book)):
        phone[i] = phone_book[i]
    
    phone_list = sorted(phone.values())  

    for i in range(len(phone_list) - 1):
        if phone_list[i+1].startswith(phone_list[i]): 
            return False
    
    return answer
