def maximo(a, b):
    max = a if a > b else b
    print(max)

def max3(a, b, c):
    max = a if a > b and a > c else b if b > a and b > c else c if c > b and c > a else a
    print(max)

def contar(iterable):
    result = 0
    for i in iterable:
        result += 1
    return result

def vocal(letra):
    return letra in "aeiouAEIOU"

def sumar(lista):
    total = 0
    for numero in lista:
        total += numero
    print(total)

def multiplicar(lista):
    total = 1
    for numero in lista:
        total *= numero
    print(total)

def invertir(string):
    resultado = ""
    for caracter in range(len(string) - 1, -1, -1):
        resultado += string[caracter]
    return resultado
        
def palindromo(palabra):
    print(invertir(palabra) == palabra)

def superposicion(lista1, lista2):
    for i in lista1:
        if i in lista2:
            return True
    return False

def generarCaracteres(num, string):
    return string * num

def histograma(lista):
    for i in lista:
        print("*"*i)
        
def piramide(num):
    for i in range(num):
        print("*"* (i + 1))
    for i in range(num -1, -1, -1):
        print("*"* i)


