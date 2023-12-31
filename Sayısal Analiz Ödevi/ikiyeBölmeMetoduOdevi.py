def f(x):
    return x*3 - 2*x*2 - 5

def ikiye_bolme(a, b, tol, max_iter):
    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c
a = 2
b = 4
tolerans = 0.0001
max_iterasyon = 4

kok = ikiye_bolme(a, b, tolerans, max_iterasyon)
print(f"[2,4] aralığında bulunan kök: {kok}")






