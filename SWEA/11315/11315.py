import sys
sys.stdin = open('sample_input.txt')

# 테스트 케이스 수
T = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, T + 1):
    N = int(input())  # 보드의 크기
    board = [input() for _ in range(N)]  # NxN 배열

    # 돌의 수 지정
    stones = 0

    # 4가지 방향(가로, 세로, 우하향, 좌하향) 델타값
    di = [0, 1, 1, 1]
    dj = [1, 0, 1, -1]

    # 보드의 크기만큼 반복 - 행 먼저 순회
    for i in range(N):
        for j in range(N):

            # 현재 칸이 'o'면
            if board[i][j] == 'o':

                # 4가지 방향을 순회
                for p in range(4):
                    count = 1  # 초기값을 1로 지정

                    # 4칸 앞까지 반복
                    for q in range(1, 5):
                        # 현재 위치를 갱신
                        ni = i + di[p] * q
                        nj = j + dj[p] * q

                        # 현재 칸이 보드 범위 내에 있고 'o'인 경우 1씩 누적
                        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                            count += 1

                    # 연속된 'o'의 개수가 5개 이상이면 돌의 수 갱신 후 종료
                    if count >= 5:
                        stones = 1

    # 최종 결과 출력
    if stones:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')