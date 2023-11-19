
import math

def f(x):
    return (4 * math.exp(-0.5 * x)) - x

def derivative_f(x, h=1e-5):
    return (f(x + h) - f(x)) / h

def newton_raphson_method(x0, tol, max_iter):
    iter_count = 0
    x = x0
    
    while True:
        if derivative_f(x) == 0:
            print("Türev sıfır olduğu için bölme hatası oluştu.")
            return None
        
        x_next = x - f(x) / derivative_f(x)
        
        if abs(x_next - x) < tol or iter_count >= max_iter:
            return x_next
        
        x = x_next
        iter_count += 1
initial_guess = 2
tolerance = 1e-8  
max_iterations = 4

root = newton_raphson_method(initial_guess, tolerance, max_iterations)
if root is not None:
    print(f"Newton-Raphson ile bulunan kök: {root}")
