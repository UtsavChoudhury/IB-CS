def f(n):
    print(n)
    if n % 2 == 0:
        f(n // 2)

f(24)

def g(n):
    if n % 2 == 0:
        g(n //2)
    print(n)