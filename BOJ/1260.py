def dfs(visited, curr_node, result):
    visited_dfs[curr_node] = 1  # 현재 지점 방문 표시
    result.append(curr_node)  # 결과에 현재 정점 넣기

    # 인접하고 미방문인 정점을 재귀 호출
    for neighbor in adj_list[curr_node]:
        if visited[neighbor] == 0:
            dfs(visited, neighbor, result)


def bfs(visited, start_node, result):
    q = [start_node]  # 큐 생성 - 시작점 인큐
    visited[start_node] = 1  # 시작점 방문 표시
    result.append(start_node)  # 시작점 넣기

    # 탐색할 정점이 없을 때까지 반복
    while q:
        current_node = q.pop(0)  # 디큐

        # 인접하고 미방문인 정점을 인큐, 방문 표시, 결과에 담기
        for neighbor in adj_list[current_node]:
            if visited[neighbor] == 0:
                q.append(neighbor)
                visited[neighbor] = 1
                result.append(neighbor)
    return


N, M, V = map(int, input().split())  # 정점의 수, 간선의 수, 시작 번호
adj_list = [[] for _ in range(N+1)]  # 1~N까지를 담을 인접 리스트
# 간선의 수만큼 반복하며 양방향으로 저장
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# 정점 번호가 작은 것을 먼저 방문해야 함 - 인접 리스트를 오름차순으로 정렬
for i in range(1, N+1):
    adj_list[i].sort()

# DFS 실행 - 함수 호출 및 결과 출력
visited_dfs = [0] * (N + 1)  # 방문 기록
result_dfs = []  # 결과 기록
dfs(visited_dfs, V, result_dfs)
print(*result_dfs)

# BFS 실행 - 함수 호출 및 결과 출력
visited_bfs = [0] * (N + 1)  # 방문 기록
result_bfs = []  # 결과 기록
bfs(visited_bfs, V, result_bfs)
print(*result_bfs)