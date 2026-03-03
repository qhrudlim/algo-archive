N, M = map(int, input().split())  # N, M 크기
board = [input() for _ in range(N)]  # 보드 상태

# 결과를 위한 변수를 무한대로 지정
result = float('inf')

# 8x8의 시작점이 될 수 있는 곳 탐색 - 행 먼저 순회
for i in range(N-7):
    for j in range(M-7):

        # 8x8의 시작점이 흰색인 경우와 검은색인 경우를 모두 계산하기 위한 것
        start_W = 0
        start_B = 0

        # 8x8 보드를 탐색 - 행 먼저 순회
        for p in range(8):
            for q in range(8):
                # 올바른 색상인지 확인 - p와 q의 합이 짝수면 시작점과 같은 색
                # 흰색으로 시작하는 경우
                if (p + q) % 2 == 0:
                    correct_pattern_w = 'W'
                else:
                    correct_pattern_w = 'B'

                # 검은색으로 시작하는 경우
                if (p + q) % 2 == 0:
                    correct_pattern_b = 'B'
                else:
                    correct_pattern_b = 'W'

                # 현재 칸의 색
                current_color = board[i + p][j + q]

                # 현재 칸의 색과 올바른 칸의 색이 다른 경우를 세기
                # 흰색으로 시작하는 경우
                if current_color != correct_pattern_w:
                    start_W += 1

                # 검은색으로 시작하는 경우
                if current_color != correct_pattern_b:
                    start_B += 1

        # 최솟값 지정
        min_count = min(start_W, start_B)
        result = min(min_count, result)

# 결과 출력
print(result)