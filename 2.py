import math
a, b, c = map(int, input("Entre com a 3 números : ").split())

if a >= (b + c) or b >= (a + c) or c >= (a + b):

    print("NAO FORMA TRIANGULO")
    print(a, b, c)
else:
    s = float((1 / 2) * (a + b + c))
    Area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print("Aréa: ", Area)
