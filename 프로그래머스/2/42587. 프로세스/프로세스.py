from collections import deque

def solution(priorities, location):
    answer = 0
    answer_list = []
    q = deque(range(len(priorities)))  
    max_value = max(priorities)  

    while q:
        q_pop = q.popleft()
        if priorities[q_pop] == max_value:  
            answer_list.append(q_pop)
            priorities[q_pop] = -1  
            answer += 1
            
            if q_pop == location: 
                return answer

            max_value = max(priorities)  
        else:
            q.append(q_pop)

    return answer