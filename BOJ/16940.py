# BFS 스페셜 저지
from collections import deque


def bfs(start_node, node_length):
    # 큐 생성 및 시작 노드를 큐에 추가, 시작점의 방문 기록 표시
    q = deque([start_node])
    visited[start_node] = 1

    # gemini
    order_map = {node: i for i, node in enumerate(visited_order)}
    for i in range(1, node_length + 1):
        adj_lst[i].sort(key=lambda x: order_map.get(x, float('inf')))

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 빼고 결과에 넣기
        t = q.popleft()
        result.append(t)

        # 현재 노드와 인접한 노드를 순회
        for w in adj_lst[t]:
            # 해당 노드를 방문한 적 없으면 큐에 추가 후 방문 기록 갱신
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1
    return


N = int(input())  # 정점 개수

# 인접 리스트 생성 후 양방향으로 저장
adj_lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)

# 방문 순서
visited_order = list(map(int, input().split()))

# 결과를 담을 빈 리스트, 방문 기록 여부
result = []
visited = [0] * (N + 1)

# 방문 순서의 첫번째는 무조건 1이어야 함
# 1이 아니면 0을 출력
if visited_order[0] != 1:
    print(0)

# 1이면 함수 호출 결과와 방문 순서가 같다면 1, 다르면 0 출력
else:
    bfs(1, N)

    if result == visited_order:
        print(1)
    else:
        print(0)