# 트리 순회

# 전위 순회
def pre_order(node):
    # 종료 조건: 현재 노드가 .이면 종료
    if node == '.':
        return

    # 아니면 현재 노드 출력 후 왼쪽->오른쪽 순으로 재귀 호출
    print(node, end='')
    pre_order(tree[node][0])
    pre_order(tree[node][1])


# 중위 순회
def in_order(node):
    # 종료 조건: 현재 노드가 .이면 종료
    if node == '.':
        return

    # 아니면 왼쪽 재귀 호출 후 현재 노드 출력, 오른쪽 재귀 호출
    in_order(tree[node][0])
    print(node, end='')
    in_order(tree[node][1])


# 후위 순회
def post_order(node):
    # 종료 조건: 현재 노드가 .이면 종료
    if node == '.':
        return

    # 아니면 왼쪽->오른쪽으로 재귀 호출 후 현재 노드 출력
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end='')


N = int(input())  # 노드 개수
tree = {}  # 트리 정보를 담을 빈 딕셔너리

# 노드 수 만큼 반복하며
# 부모노드, 왼쪽 자식 노드, 오른쪽 자식 노드를 받아 트리에 저장
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

# 전위 순회 함수 호출
pre_order('A')
print()

# 중위 순회 함수 호출
in_order('A')
print()

# 후위 순회 함수 호출
post_order('A')