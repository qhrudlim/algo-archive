# 너구리 구구

from collections import deque


def bfs(curr_node, curr_distance):
    global max_distance

    # 시작점을 큐에 넣기
    q = deque([(curr_node, curr_distance)])

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 뺀 값을 현재 노드와 현재까지의 거리로 지정 및 최대 거리 갱신
        curr_node, curr_distance = q.popleft()
        max_distance = max(max_distance, curr_distance)

        # 현재 노드를 반복하며 이미 방문했으면 종료
        for neighbor, distance in graph[curr_node]:
            if visited[neighbor]:
                continue

            # 방문하지 않았으면 방문 처리 후 해당 노드와 현재까지의 거리를 큐에 넣기
            visited[neighbor] = 1
            q.append((neighbor, curr_distance+distance))

    # 최대 거리 반환환
    return max_distance


N = int(input())  # 방 개수
graph = [[] for _ in range(N+1)]  # 인접 리스트 - 연결된 간선 저장
visited = [0] * (N+1)
visited[1] = 1
max_distance = 0

# N-1만큼 반복하며 방 정보와 연결 길이를 입력받은 후 양방향으로 저장
for _ in range(N-1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

# 함수 호출 및 결과 출력
result = bfs(1, 0)
print(result)