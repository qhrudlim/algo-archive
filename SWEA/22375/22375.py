import sys
sys.stdin = open('switch_sample_in.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 스위치 개수

    # 조작 전 스위치 상태, 조작 후 스위치 상태
    A, B = [list(map(int, input().split())) for _ in range(2)]

    switch_count = 0  # 스위치 조작 횟수를 0으로 설정

    for i in range(N):  # N번 반복
        if A[i] != B[i]:  # 현재 상태와 조작 후 상태가 다르면
            switch_count += 1  # 스위치 조작 횟수를 1 증가

            for j in range(i, N):  # i부터 N-1번까지 반복
                if A[j] == 0:  # 현재 상태가 0이면
                    A[j] = 1  # 현재 상태를 1로
                else:  # 현재 상태가 1이면
                    A[j] = 0  # 현재 상태를 0으로
    
    print(f'#{tc}', switch_count)  # 결과 출력