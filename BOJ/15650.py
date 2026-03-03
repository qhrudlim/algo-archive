import sys


def find_sequence(start_num, result):
    # 종료 조건 - 모든 원소 선택시 결과 출력
    if len(result) == M:
        print(*result)
        return

    # 시작 번호부터 끝 번호까지 반복하며
    # 현재 번호를 결과에 넣고,
    # 다음 번호를 재귀 호출
    # 다음 경우를 위해 마지막 숫자 제거
    for n in range(start_num, N + 1):
        result.append(n)
        find_sequence(n + 1, result)
        result.pop()


N, M = map(int, sys.stdin.readline().split())  # 전체 수, 해당 조건의 길이
results = []  # 결과를 담을 리스트
find_sequence(1, results)  # 함수 호출