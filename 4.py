def primo(n, count):
    if n % count == 0:
        return True

    else:
        return False


n = 100
for count in range(2, n + 1):
    print(primo(n, count))
