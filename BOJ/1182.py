def find_S(idx, current_sum):
    global count

    # 종료 조건 - 모든 원소 탐색 시 종료
    if idx == N:
        return

    # 현재 값과 현재까지의 합이 S와 같으면 count 누적
    if arr_num[idx] + current_sum == S:
        count += 1

    # 현재 값을 포함하고 다음으로 넘어가는 재귀 호출
    find_S(idx + 1, current_sum + arr_num[idx])

    # 현재 값을 포함하지 않고 다음으로 넘어가는 재귀 호출
    find_S(idx + 1, current_sum)


N, S = map(int, input().split())  # N, S
arr_num = list(map(int, input().split()))  # 정수 배열
count = 0  # 합이 S가 되는 부분 수열을 셀 변수
find_S(0, 0)  # 함수 호출 - 0번째 인덱스, 초기 합:0
print(count)  # 결과 출력