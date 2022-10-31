a, b, c = map(int, input("Entre com a 3 números : ").split())

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)
