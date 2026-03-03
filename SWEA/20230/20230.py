import sys
sys.stdin = open('sample_in.txt')

T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):  # 테스트 케이스만큼 반복
    N = int(input())  # 격자의 크기
    
    stage_list = []  # 배열을 담을 빈 리스트 생성
    for i in range(N):  # 격자의 크기만큼 반복
        arr = list(map(int, input().split()))  # NxN 배열
        stage_list.append(arr)  # 배열을 리스트에 넣기
        
    max_score = 0  # 최대 점수를 0으로 설정
    for i in range(N):  # 행 먼저 순회
        for j in range(N):  # 열 순회
            current_score = 0  # 현재 점수를 0으로 설정

            row_sum = 0  # 행의 합을 0으로 설정
            for r in range(N):  # 행 전체를 반복
                # 행의 합에 리스트의 ir번째 값 누적
                row_sum += stage_list[i][r]
            
            col_sum = 0  # 열의 합을 0으로 설정
            for c in range(N):  # 열 전체를 반복
                # 열의 합에 리스트의 cj번째 값 누적
                col_sum += stage_list[c][j]
            
            # 현재 점수를 행의 합 + 열의 합 - 중복되는 값(중간 값)으로 계산
            current_score = row_sum + col_sum - stage_list[i][j]
            
            if  current_score > max_score:  # 현재 점수가 최대 점수보다 크다면
                max_score = current_score  # 최대 점수를 현재 점수로 갱신
                
    print(f'#{tc}', max_score)  # 결과 출력