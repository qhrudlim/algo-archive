import sys
input = sys.stdin.readline

N = int(input())
# 출입 기록의 수 
employee_status = set()
#set으로 출근한 사람들 모아두기
for i in range(N):
    name, behavior = input().split()
    #입력 예제에서 split해서 name과 behavior에 할당하기
    if behavior == 'enter':
        employee_status.add(name)
    else:
        employee_status.remove(name)
        
for person in sorted(employee_status, reverse=True):
# set에서는 메서드 이용이 어려우니 리버스해서 하나씩 꺼내야한다.
    print(person)

