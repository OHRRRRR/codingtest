# X일 동안 가장 많이 들어온 방문자 수와 기간
# 시작하고 지난일수 n x
# 1일차부터 n일차까지 하루 방문자 수

# x일 동안 가장 많이 들어온 방문자 수 출력
# 만약 최대 방문자 수 0이면 SAD 출력
# 최대 방문자 수 0아니면 둘째 줄에 기간 몇 개 있는지 출력

# n일 중 x씩 묶었을때 최대가 되는 값 출력
# 방문자 수 > 0이면 기간 몇개 있는지 출력
import sys
input = sys.stdin.readline

n,x = map(int,input().split())
data = list(map(int,input().split()))

if max(data) == 0: #방문자 최대값 0일때 SAD
    print("SAD")
else:
    value = sum(data[:x]) #0부터 x개의 합 #0부터4까지합
    # 첫 x일 동안 방문자 수의 합계 저장 #5일동안

    max_value = value #최고 방문자 수 초기화
    max_cnt = 1 #최대 방문자 수 

    #슬라이딩 윈도우 통한 방문자 수 계산
    for i in range(x,n):#x5n7
        value += data[i] #현재 i일차의 방문자수 value에 추가
        value -= data[i-x] #슬라이딩 윈도우의 시작날을 value에서 뺌

        # 최대 방문자 수와 그 기간 개수 계산
        if value > max_value: # 현재 윈도우의 방문자 수가 기존 최대값보다 크면
            max_value=value #max_value갱신
            max_cnt = 1 #max_cnt로 1로 초기화
        elif value == max_value: #현재 윈도우의 방문자 수가 기준 최대값과 최대값을 기록한 기간의 개수 증가
            max_cnt += 1
    print(max_value)
    print(max_cnt)