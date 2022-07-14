#!usr/bin/env python3
"""
criar um codigo que imprime numeros pares de 1 ao 200
exemplo :
2
4
6
8
10
12
14
16
etc, etc, etc, etc, 
"""
for num in range(1,201):
    if num % 2 != 0: 
        continue
    print(num)
