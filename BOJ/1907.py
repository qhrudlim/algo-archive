# 탄소 화합물

import sys
input = sys.stdin.readline


def analyze_composition(molecule_formula):
    # 원자 개수를 담을 딕셔너리, 인덱스 초기화
    element_cnt = {'C': 0, 'H': 0, 'O': 0}
    idx = 0

    # 인덱스가 화학식의 길이보다 커질 때까지 반복
    while idx < len(molecule_formula):
        # 화학식의 요소 지정
        element = molecule_formula[idx]

        # 인덱스 증가 및 원자성(원소 뒤에 오는 숫자)을 담을 문자열 초기화
        idx += 1
        atomicity = ''

        # 인덱스가 화학식 길이 이상이거나 해당 요소가 원자가 될 때까지 반복
        while idx < len(molecule_formula) and molecule_formula[idx].isdigit():
            # 원자성에 해당 숫자 누적 및 인덱스 증가
            atomicity += molecule_formula[idx]
            idx += 1

        # 원자성이 있으면 원자성을, 아니면 1을 원자의 개수로 두고, 원자 개수에 원자성 누적
        atom_cnt = int(atomicity) if atomicity else 1
        element_cnt[element] += atom_cnt

    # 탄소, 수소, 산소의 원자 개수 반환
    return [element_cnt['C'], element_cnt['H'], element_cnt['O']]


# 화학 반응식 분리 입력 (반응물(x,y)과 생성물로 분리)
reactant, z = input().strip().split('=')
x, y = reactant.split('+')

# 각 분자의 원자 조성 분석
x_cnt = analyze_composition(x)
y_cnt = analyze_composition(y)
z_cnt = analyze_composition(z)

# 가능한 계수를 못 찾았다고 가정
possible_coeff = False

# 각 분자를 가능한 계수(1~10)만큼 탐색하며
# 각 원소의 균형 확인 후 균형이면 해당 계수 출력 및 가능하다고 표시
# 아니면 반복문 종료
for x_coeff in range(1, 11):
    for y_coeff in range(1, 11):
        for z_coeff in range(1, 11):
            C_bal = (x_cnt[0] * x_coeff + y_cnt[0] * y_coeff == z_cnt[0] * z_coeff)
            H_bal = (x_cnt[1] * x_coeff + y_cnt[1] * y_coeff == z_cnt[1] * z_coeff)
            O_bal = (x_cnt[2] * x_coeff + y_cnt[2] * y_coeff == z_cnt[2] * z_coeff)
            if C_bal and H_bal and O_bal:
                print(x_coeff, y_coeff, z_coeff)
                possible_coeff = True
                break
        if possible_coeff:
            break
    if possible_coeff:
        break