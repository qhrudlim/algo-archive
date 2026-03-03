# A → B

A, B = map(int, input().split())
cnt = 0  # count 초기화

# A가 B 이상이 될 때까지 반복
while A < B:
    # B의 마지막 자리가 1이면 B를 10으로 나눈 몫으로 갱신 후 count 증가
    if B % 10 == 1:
        B //= 10
        cnt += 1

    # B가 짝수면 B를 2으로 나눈 몫으로 갱신 후 count 증가
    elif B % 2 == 0:
        B //= 2
        cnt += 1

    # 그 외의 경우에는 count를 초기화 후 종료
    else:
        cnt = 1
        break

# 반복 종료 후 B가 A와 같아지면 count에 1을 더한 값 출력
if B == A:
    print(cnt+1)

# 아니면 -1 출력
else:
    print(-1)