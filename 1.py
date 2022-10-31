d = int(input("Entre com a idade em dias: "))
a = int(d / 365)
d %= 365
m = int(d / 30)
d %= 30
print(a, " ano(s)")
print(m, " mes(es)")
print(d, " dia(s)")
