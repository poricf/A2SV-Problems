t = int(input())

for _ in range(t):
    a, b, l = map(int, input().split())

    posk = set()

    for i in range(l + 1):
        pow_a = pow(a, i)
        if pow_a > l:
            break

        for y in range(l + 1):
            value = pow_a * pow(b, y)
            if value > l:
                break

            if l % value == 0:
                posk.add(l // value)
    ans = len(posk)
    print(ans)