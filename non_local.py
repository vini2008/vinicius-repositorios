contador = 0

def funcao():
    global contador
    contador += 1

    def funcao_interna():
        global contador
        contador += 1
    
    funcao_interna()

funcao()
funcao()

print(contador)
