def solution(phone_book):
    phone = {}
    
    for i in phone_book:
        phone[i] = 1
            
    for nums in phone_book:
        arr = ""
        for i in nums:
            arr += i
            if arr in phone and arr != nums:
                return False
            
    return True