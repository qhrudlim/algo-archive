# 0의 개수
N = int(input())

def count_zeros(N):
    if N == 0:
        return 0

    count = 0
    while N > 0:
        N = N // 5
        count += N
    return count

print(count_zeros(N))