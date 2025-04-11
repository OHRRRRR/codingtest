def solution(n, computers):
    
    def dfs(v):
        visited[v]=1
        for k in range(n):
            if not visited[k] and computers[v][k]==1:
                dfs(k)
    
    answer = 0
    visited = [0]*n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer