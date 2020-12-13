from prettytable import PrettyTable

inp = list(
    map(int,
        input('Enter integers in form: ax = c (mod m) ').split()))
inp = list(map(abs, inp))
c = inp.pop(1)
m = inp[1]
a, b = max(inp), min(inp)
x, y, r, q = [1, 0], [0, 1], [a, b], [0, 0]

t = PrettyTable(['x', 'y', 'r', 'q'])
t.add_row([x[-2], y[-2], r[-2], q[-2]])
t.add_row([x[-1], y[-1], r[-1], q[-1]])

while (x[-1] * a + y[-1] * b):
    q.append(int(r[-2] / r[-1]))
    r.append(r[-2] % r[-1])
    x.append(x[-2] - x[-1] * q[-1])
    y.append(y[-2] - y[-1] * q[-1])
    t.add_row([x[-1], y[-1], r[-1], q[-1]])

print(t)

gcd = r[-2];
print(f"GCD: {gcd}")


if c % gcd == 0:
	x0, y0 = x[-2] * int((c/gcd)), y[-2] * int((c/gcd))
	print(x0, y0)
	if (a == inp[0]):
		k = x0 % m
	else:
		k = y0 % m
	print(f"There are {gcd} distinct solutions. The solutions are:")
	print(inp)
	for i in range (gcd):
		print(k + i * int(m/gcd), end=" ")
else:
	print(f'No solution, {gcd} does not divide {c}')
