def solve():
    n = int(input())

    company_status = {}
    for _ in range(n):
        name, status = input().split()

        if status == "enter":
            company_status[name] = True

        elif status == "leave":
            if name in company_status:
                del company_status[name]

    current_employees = []
    for name in company_status:
        current_employees.append(name)

    num_employees = 0
    for _ in current_employees:
        num_employees += 1

    current_employees.sort(reverse=True)

    for name in current_employees:
        print(name)

solve()