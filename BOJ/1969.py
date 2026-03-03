# DNA

N, M = map(int, input().split())  # dna 수, 문자열 길이
dna_lst = [input() for _ in range(N)]  # dna 리스트

hamming_distance = 0  # h.d 초기화
result_dna = ''  # 결과를 담을 문자열

# 문자열 길이만큼 반복
for j in range(M):
    # 염기 서열별로 개수를 담을 딕셔너리
    dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # dna 문자열을 반복하며 현재 위치의 염기 서열 개수 세기
    for i in range(N):
        dna_dict[dna_lst[i][j]] += 1

    # 가장 많이 나오는 염기를 찾기 위한 변수 초기화
    max_cnt = 0
    max_dna = ''

    # 사전 순으로 정렬된 염기를 반복하며 가장 많이 나온 염기 갱신
    for dna in sorted(dna_dict.keys()):
        if dna_dict[dna] > max_cnt:
            max_cnt = dna_dict[dna]
            max_dna = dna

    # 결과 문자열에 가장 많이 나온 염기 추가
    result_dna += max_dna

    # hamming distance 계산 (전체 개수에서 가장 많이 나온 개수를 뺀 것)
    hamming_distance += (N - max_cnt)

# 결과 출력
print(result_dna)
print(hamming_distance)