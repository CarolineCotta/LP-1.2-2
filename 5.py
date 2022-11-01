inverte = ""
frase = input('Digite uma frase: ')  
for palavra in frase.split(" "):
    inverte += palavra[::-1] + " "
print(format(inverte))
