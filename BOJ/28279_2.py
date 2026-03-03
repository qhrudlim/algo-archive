n1, n2 = map(int, input().split())
i1 = (n1 - 1) % 4
j1 = (n1 - 1) // 4
i2 = (n2 - 1) % 4
j2 = (n2 - 1) // 4
print(abs(i1 - i2) + abs(j1 - j2))


n1, n2 = map(int, input().split())
n1 -= 1
n2 -= 1
print(abs(n1//4 - n2//4) + abs(n1%4 - n2%4))