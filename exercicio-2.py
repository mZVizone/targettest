def is_fibonacci(f):
    if f <= 1:
        return True
    a, b = 0, 1
    while b < f:
        a, b = b, a + b
    return b == f
sec = int(input("Por favor digite um número inteiro: "))
if is_fibonacci(sec):
    print(sec, "faz parte da sequência de Fibonacci.")
else:
    print(sec, "não faz parte da sequência de Fibonacci.")