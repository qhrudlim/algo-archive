# 미로 탐색

import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    # 큐에 시작점을 넣고, 시작점에 방문 기록
    q = deque([(0, 0)])
    visited[0][0] = 1

    # 델타 값
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 뺀 값 지정 (위치값)
        r, c = q.popleft()

        # 도착점에 도착 시 이동 횟수 반환
        if r == N - 1 and c == M - 1:
            return visited[r][c]

        # 상하좌우를 탐색하며 새 위치 지정
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            # 범위 내에 없거나, 벽이거나, 이미 방문한 곳이면 다음 위치로
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if maze[nr][nc] == 0:
                continue

            if visited[nr][nc] != 0:
                continue

            # 이동 횟수 증가 후 큐에 추가
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

    # 그 외에는 -1 반환
    return -1


# 미로의 크기 및 미로 정보
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# 방문 기록 및 이동 횟수 저장
visited = [[0] * M for _ in range(N)]

# 함수 호출 및 결과 출력
print(bfs())