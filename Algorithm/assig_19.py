def solution(n):

    num = n ** 0.5

    if num == int(num):
        return (num+1)**2
    else:
        return -1

print(solution())


num = range(1,90)
b = []
for i in num:
    p = i ** 0.5
    if p == int(p):
        b.append((p+1)**2)
    else:
        b.append(-1)

print(b)
