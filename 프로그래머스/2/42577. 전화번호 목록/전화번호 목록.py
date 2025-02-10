def solution(phone_book):
    answer = True
    phone = {}
    cnt = 0
    
    for i in range(len(phone_book)):
        phone[i] = phone_book[i]
    
    phone_list = sorted(phone.values())  # 전화번호를 정렬하여 사전순으로 정리

    for i in range(len(phone_list) - 1):
        if phone_list[i+1].startswith(phone_list[i]):  # 인접한 번호끼리 접두어 여부 확인
            return False
    
    return answer