#! usr/bin/env python3
"""Exemplos de funçoes"""
"""
f(x) = 5 * (X/2)
"""


# SOLID -Single Responsibility

def f(x): # assinatura
  result = 5 * (x / 2) 
  ...
  return result


def double(x):
    return x * 2

valor = double(f(10))

print(valor)
print(valor == 25)


def print_in_upper(text):
    """Produre with no explicit return"""
    print(text.upper())
    # implict return None

print_in_upper("bruno")



####


def heron(a,b,c):
    """Caucula a Area de um Triangulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)    

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
] 

for t in triangulos:
    area = heron(*t)
    print(f"A area do triangulo é: {area}")



#####

def nome_da_funcao():
    print("Hello funcao")
    return 1 

result = nome_da_funcao()
print(result)













