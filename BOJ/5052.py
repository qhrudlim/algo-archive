# 전화번호 목록

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 전화번호 수
    num_lst = [input().strip() for _ in range(N)]  # 전화번호
    num_lst.sort()  # 오름차순으로 정렬
    result = 'YES'  # 결과 초기화

    # N보다 하나 적게 반복하며 현재 수가 다음 수에 포함되면 NO를 출력
    for i in range(N-1):
        if num_lst[i] == num_lst[i+1][:len(num_lst[i])]:
            result = 'NO'

    # 결과 출력
    print(result)