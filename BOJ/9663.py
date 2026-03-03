# N-Queen

def is_checked(curr_row):
    # 이전 행들을 순회하며 놓일 수 있는 지 확인
    for pre_row in range(curr_row):
        # 같은 열에 놓인 상태이면 실패
        if board[curr_row] == board[pre_row]:
            return False

        # 같은 대각선에 놓인 상태이면 실패
        if abs(curr_row - pre_row) == abs(board[curr_row] - board[pre_row]):
            return False

    # 나머지는 모두 성공 (놓일 수 있음)
    return True


def dfs(row):
    global cnt

    # 종료 조건: 모든 행에 퀸을 배치하면 개수 증가 후 종료
    if row == N:
        cnt += 1
        return

    # 열을 반복
    for col in range(N):
        # 해당 열을 방문했으면 다음 열로 이동
        if visited[col]:
            continue

        # 배열에 행과 열 지정
        board[row] = col

        # 행에 놓을 수 있으면
        # 해당 열의 방문 기록을 표시하고 재귀 호출 후 방문 기록 제거
        if is_checked(row):
            visited[col] = 1
            dfs(row + 1)
            visited[col] = 0


N = int(input())  # 퀸 개수
board = [0] * N  # 보드 배열
visited = [0] * N  # 방문 기록
cnt = 0  # 개수 초기화
dfs(0)  # 함수 호출
print(cnt)  # 개수 출력