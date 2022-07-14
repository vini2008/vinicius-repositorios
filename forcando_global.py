nome = "Global"


def funcao():
    nome = "Local"
    print("nome local:", nome)
    nome = globals()["nome"] 
    print("nome Global:", nome)


funcao()

    
