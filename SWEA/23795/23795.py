import sys
sys.stdin = open('sample_in.txt')

T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 격자 크기
    # NxN 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    monster = None  # 괴물 위치를 None으로 설정
    for i in range(N):  # 행 먼저 순회
        for j in range(N):  # 열 순회

            if arr[i][j] == 2:  # 현재 위치가 2라면
                monster = (i, j)  # 괴물 위치를 현재 위치로 바꾸고 종료
                break

        if monster:  # 괴물 위치가 있다면 종료
            break

    # False로 채워진 광선이 닿는 칸 표시용 배열
    lights = [[False] * N for _ in range(N)]

    # 배열에서 괴물이 있는 위치를 True로 변경
    lights[monster[0]][monster[1]] = True

    # 델타 값(상하좌우)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):  # 방향 순회
        ni, nj = monster  # 각 방향별 위치를 괴물 위치로 지정

        while True:  # True가 될 때까지 반복
            # 방향별의 위치값에 델타값 누적
            ni += di[k]
            nj += dj[k]

            # 유효하지 않은 범위면 종료
            if not (0 <= ni < N and 0 <= nj < N):
                break

            # 배열의 방향별 위치 값이 1이면 종료
            if arr[ni][nj] == 1:
                break

            # 광선의 위치를 True로 지정
            lights[ni][nj] = True  # 광선이 닿음

    count_safe = 0  # 안전한 칸의 수를 0으로 지정
    for i in range(N):  # 행 먼저 순회
        for j in range(N):  # 열 순회

            # 배열의 현재값이 0이고, 광선의 위치가 없으면
            if arr[i][j] == 0 and not lights[i][j]:
                count_safe += 1  # 안전한 칸의 수를 1씩 누적

    print(f'#{tc}', count_safe)  # 결과 출력
