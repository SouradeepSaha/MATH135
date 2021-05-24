from prettytable import PrettyTable


def EEA(num1, num2):
    a, b = max(num1, num2), min(num1, num2)
    x, y, r, q = [1, 0], [0, 1], [a, b], [0, 0]

    t = PrettyTable(['x', 'y', 'r', 'q'])
    t.add_row([x[-2], y[-2], r[-2], q[-2]])
    t.add_row([x[-1], y[-1], r[-1], q[-1]])

    while x[-1] * a + y[-1] * b:
        q.append(int(r[-2] / r[-1]))
        r.append(r[-2] % r[-1])
        x.append(x[-2] - x[-1] * q[-1])
        y.append(y[-2] - y[-1] * q[-1])
        t.add_row([x[-1], y[-1], r[-1], q[-1]])
    print("EEA Table: ")
    print(t)
    return [x, y, r, q]


def LDET(a, b, c):
    table = EEA(a, b)
    gcd = table[2][-2]
    print(f"GCD: {gcd}")
    if c % gcd == 0:
        x0, y0 = table[0][-2] * int((c / gcd)), table[0][-2] * int((c / gcd))
        print(f"x0 = {x0}, y0 = {y0}")
        print(f"{x0} x {a} + {y0} x {b} = {int(c / gcd)}\n")
        print(f"All solutions for x: {x0} + {int(b / gcd)}n")
        print(f"All solutions for y: {y0} - {int(a / gcd)}n")
    else:
        print('No solution')

    print(f"GCD: {gcd}")


def LCT(a, b, m):
    table = EEA(a, m)
    gcd, x, y = table[2][-2], table[0], table[1]
    print(f"GCD: {gcd}")

    if b % gcd == 0:
        c = int((b / gcd))
        if a == table[2][0]:
            x0 = (x[-2] * c) % m
        else:
            x0 = (y[-2] * c) % m
        print(f"There are {gcd} distinct solutions. The solutions are:")
        for i in range(gcd):
            print(x0 + i * int(m / gcd), end=" ")
        print('\n---END OF SOLUTIONS---')
    else:
        x0 = 'invalid'
        print(f'No solution, {gcd} does not divide {b}')
    return x0


def pubKey(p,q,e):
    n = p * q
    print(f"Public key (e,n)=({e}, {n})")
    return [e, n]

def priKey(p, q, e):
    n = p * q
    sp = (p-1) * (q-1)
    d = LCT(e, 1, sp)
    print(f"Private key (d,n)=({d}, {n})")
    return[d, n]


def powerMod(base, exp, m):
    a1 = base % m
    p = 1
    while exp > 0:
        if exp % 2:
            p *= a1
            p = p % m
        exp = int(exp/2)
        a1 = (a1 * a1) % m
    return p
