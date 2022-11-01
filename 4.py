def primos(n):
    for count in range(1, n+1):
        if n % count == 0:
            print("é primo", count)
            return True
        else:
            print("não é", count)
            return False


print(primos(100))
