def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

a = prime(9)
print(a)