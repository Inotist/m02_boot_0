def cuadrado(x):
    return x*x

def cubo(x):
    return x**3

def sumaTodos(limitTo, f=lambda x: x):
    resultado = 0
    for i in range(1, limitTo+1):
        resultado += f(i)
        
    return resultado

if __name__ == '__main__':
    print(sumaTodos(100))
    print(sumaTodos(3, cuadrado))