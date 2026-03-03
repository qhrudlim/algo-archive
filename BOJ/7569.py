# 토마토

import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    # 큐 생성 및 전체를 돌며 토마토가 있으면 해당 좌표를 큐에 넣기
    q = deque()
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if box[h][r][c] == 1:
                    q.append((h, r, c))

    # 델타 값
    dh = [0, 0, 0, 0, -1, 1]
    dr = [-1, 1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 뺀 값 지정 (위치값)
        h, r, c = q.popleft()

        # 상하좌우를 탐색하며 새 위치 지정
        for k in range(6):
            nh, nr, nc = h + dh[k], r + dr[k], c + dc[k]

            # 범위 내에 없거나 안 익은 토마토가 아니면 다음 위치로
            if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if box[nh][nr][nc] != 0:
                continue

            # 해당 토마토(안 익음)의 일수 증가 및 큐에 넣기
            box[nh][nr][nc] = box[h][r][c] + 1
            q.append((nh, nr, nc))

    # 최대 일수 초기화 및 모든 좌표를 돌며
    # 안 익은 토마토가 있으면 -1 반환, 아니면 최대 일수 갱신
    max_day = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if box[h][r][c] == 0:
                    return -1

                if box[h][r][c] > max_day:
                    max_day = box[h][r][c]

    # 최대 일수에서 시작일을 뺀 값 반환
    return max_day - 1


# 상자의 크기 및 상자의 수, 토마토 정보
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 함수 호출 및 결과 출력
print(bfs())