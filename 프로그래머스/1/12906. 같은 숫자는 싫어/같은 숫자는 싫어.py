import sys
input = sys.stdin.readline

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            answer.append(arr[i])
    return answer


# import sys
# from collections import deque

# input = sys.stdin.readline

# def solution(arr):
#     answer = []
    
#     # 길이가 1 이상인 경우만 처리
#     if len(arr) == 0:
#         return answer

#     for i in range(len(arr) - 1):
#         if arr[i] == arr[i + 1]:
#             if i > 0 and arr[i] == arr[i - 1]:
#                 pass
#             else:
#                 answer.append(arr[i])
#         elif arr.count(arr[i]) == 1:
#             answer.append(arr[i])
#         else:
#             pass

#     # 마지막 요소에 대한 처리
#     if arr.count(arr[-1]) == 1:
#         answer.append(arr[-1])
    
#     return answer

# arr_input = list(map(int, input().split()))
# print(solution(arr_input))