import time

def imprime_nome(nome, sobrenome="Sabugosa"):
    # escopo local {nome: .., sobrenome}
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Bruno", "rocha")
imprime_nome("maria", "tereza")


def conecta(host, timeout=10):
    print(f"conectando com {host}")
    for i in range(1, timeout):
        time.sleep(1)
        print("." * i)
    print("Erro ao conectar")


conecta("localhost")





