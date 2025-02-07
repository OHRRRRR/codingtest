from collections import Counter

def solution(participant, completion):
    answer = ''
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for key in participant_count:
        if participant_count[key] != completion_count[key]:
            answer += key
            
    return answer


