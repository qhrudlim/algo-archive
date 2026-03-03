from collections import deque


def calculate_distance(n1, n2):
    # 두 자연수 사이의 직각 거리를 계산하는 함수
    
    # 두 수를 덱에 저장
    q = deque([n1, n2])
    
    # 두 숫자의 위치(행, 열)를 저장할 스택
    stack = []
    
    # 큐가 없을 때까지 반복
    while q:
        # 큐에서 빼낸 값을 현재 수로 지정
        curr_num = q.popleft()
        
        # 계산을 위해 1을 뺀 값을 임시 수로 지정
        temp_num = curr_num - 1
        
        # 행과 열 계산
        # 행 : 임시 수를 4로 나눈 나머지에 1을 더한 값
        row = (temp_num % 4) + 1
        # 열 : 임시 수를 4로 나눈 몫에 1을 더한 값
        col = (temp_num // 4) + 1
        
        # 스택에 행과 열 넣기
        stack.append((row, col))
    
    # 스택에서 꺼낸 수를 지정
    p1 = stack.pop()
    p2 = stack.pop()
    
    # 위치 변경(뒤집어서 꺼냄)
    if n1 > n2:
        p1, p2 = p2, p1
    
    # 변경한 위치의 값을 행과 열로 분리해서 지정
    row1, col1 = p1
    row2, col2 = p2

    # 동서방향 거리와 남북방향 거리를 절댓값으로 계산
    east_west = abs(col1 - col2)
    north_south = abs(row1 - row2)
    
    # 직각 거리(동서 + 남북) 계산
    total_distance = east_west + north_south
    
    # 직각 거리 반환
    return total_distance


# 두 수 입력받기
n1, n2 = map(int, input().split())

# 함수 호출
distance = calculate_distance(n1, n2)

# 결과 출력
print(distance)