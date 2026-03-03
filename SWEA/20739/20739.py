import sys
sys.stdin = open('sample_in.txt')

T = int(input())  # 사진 데이터 개수
for tc in range(1, T+1):  # 데이터 수만큼 반복
    N, M = map(int, input().split())  # 행 수, 열 수
    # NxM 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0  # 최대 길이를 0으로 지정
    for i in range(N):  # 행 먼저 순회
        length = 0  # 현재 길이를 0으로 지정
        for j in range(M):  # 열 순회
            if arr[i][j] == 1:  # 현재 값이 1이면
                length += 1  # 현재 길이 누적
            else:  # 현재 값이 1이 아니라면
                if length > max_length:  # 현재 길이가 최장길이보다 길다면
                    max_length = length  # 최장 길이를 현재 길이로 갱신
                length = 0  # 현재 길이를 0으로 초기화

        if length > max_length:  # 현재 길이가 최장 길이보다 길다면
            max_length = length  # 최장 길이를 현재 길이로 갱신

    for j in range(M):  # 열 먼저 순회
        length = 0  # 현재 길이를 0으로 지정
        for i in range(N):  # 행 순회
            if arr[i][j] == 1:  # 현재 값이 1이면
                length += 1  # 현재 길이를 0으로 초기화
            else:  # 현재 값이 1이 아니라면
                if length > max_length:  # 현재 길이가 최장길이보다 길다면
                    max_length = length  # 최장 길이를 현재 길이로 갱신
                length = 0  # 현재 길이를 0으로 초기화

        if length > max_length:  # 현재 길이가 최장 길이보다 길다면
            max_length = length  # 최장 길이를 현재 길이로 갱신

    if max_length == 1:  # 최장 길이가 1이면
        max_length = 0  # 최장 길이를 0으로 출력 - 방문 확인

    print(f'#{tc}', max_length)  # 결과 출력