import sys
from collections import deque

N = int(sys.stdin.readline())  # 명령 수
d = deque()  # 덱 생성
for _ in range(N):  # 명령의 수만큼 반복
    order_list = sys.stdin.readline().split()
    orders = order_list[0]

    if orders == 'push_front':
        d.appendleft(int(order_list[1]))
    elif orders == 'push_back':
        d.append(int(order_list[1]))
    elif orders == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif orders == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif orders == 'size':
        print(len(d))
    elif orders == 'empty':
        if not d:
            print(1)
        else:
            print(0)
    elif orders == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif orders == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)