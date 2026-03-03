from collections import deque
import sys

input = sys.stdin.readline

# 명령의 수 받기
N = int(input())

# 큐 생성
q = deque()

# 명령의 수만큼 반복
for _ in range(N):
    # 명령 받기
    X = list(map(int, input().split()))

    # 첫번째 값이 1이라면 두번째 값을 큐의 앞에 넣기
    if X[0] == 1:
        q.appendleft(X[1])

    # 첫번째 값이 2라면 두번째 값을 큐의 뒤에 넣기
    elif X[0] == 2:
        q.append(X[1])

    # 첫번째 값이 3일 때,
    # 큐가 있으면 큐의 첫번째를 빼서 출력하고 
    # 없으면 -1을 출력
    elif X[0] == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)

    # 첫번째 값이 4일 때,
    # 큐가 있으면 큐의 마지막을 빼서 출력하고
    # 없으면 -1을 출력
    elif X[0] == 4:
        if q:
            print(q.pop())
        else:
            print(-1)

    # 첫번째 값이 5라면 큐의 길이를 출력
    elif X[0] == 5:
        print(len(q))

    # 첫번째 값이 6일 때,
    # 큐가 없으면 1을 출력하고
    # 있으면 0을 출력
    elif X[0] == 6:
        if not q:
            print(1)
        else:
            print(0)

    # 첫번째 값이 7일 때,
    # 큐가 있으면 큐의 첫번째 값을 출력하고
    # 없으면 -1을 출력
    elif X[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)

    # 첫번째 값이 8일 때,
    # 큐가 있으면 큐의 마지막 값을 출력하고
    # 없으면 -1을 출력
    elif X[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)