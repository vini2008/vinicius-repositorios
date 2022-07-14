"""
faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
import sys
import logging

RESERVAS_FILE = "reservas.txt"
Quartos_FILE = "quartos.txt"

# Acesso ao Banco de dados

# TODO: Usar pacote csv

ocupados = {} # acumulador 
try:
   for line in open(RESERVAS_FILE):
       nome_cliente, num_quarto, dias = line.strip().split(",")
       ocupados[int(num_quarto)] = {
          "nome_cliente": nome_cliente,
          "dias": int(dias)
    }   
except FileNotFoundError:
    logging.error("arquivo %s não existe", RESERVAS_FILE)
    sys.exit(1)

# TODO: Usar função para ler os arquivos

quartos = {} # acumulador
try:
    for line in open(Quartos_FILE):
       num_quarto, nome_quarto, preco = line.strip().split(",")
       quartos[int(num_quarto)] = {
          "nome_quarto": nome_quarto,
          "preco": float(preco), # TODO: Usar Decimal
          "disponivel": False if int(num_quarto) in ocupados else True,
    }   
except FileNotFoundError:
    logging.error("arquivo %s não existe", Quartos_FILE)
    sys.exit(1)


# Programa Principal
print("Reservas Do Hotel Pythonico Da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel lotado, Tente novamente mais tarde.")
    sys.exit(0)

nome_cliente = input("Digite seu nome por favor:").strip()
print()
print("Lista de Quartos:")
print()
head = ["Número","Nome do Quarto", "preço", "Disponivel"]
print(f"{head[0]:<6} - {head[1]:<14} - {head[2]:<9} - {head[3]:<10}")
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = " 🚫 " if not dados_quarto["disponivel"] else " 👍 "
    print(
         f"{num_quarto:<6} - {nome_quarto:<14} - "
         f"R$ {preco:<9.2f} - {disponivel}"
    )

print("-" * 52)
# reserva

try:
   num_quarto = int(input("Qual o quarto desejado").strip())
   if not quartos[num_quarto]["disponivel"]:
      print(f"o quarto {num_quarto} está ocupado, escolha outro.")
      sys.exit(0)
except KeyError:
    print(f"Esse quarto {num_quarto} não existe, por favor escolha outro quarto.")
    sys.exit(0)
except ValueError:
    print("Número invalido, digite apenas números.")
    sys.exit(0)

try:
    dias = int(input("Quantas dias:").strip())
except ValueError:
    print("Número invalido, digite apenas números.")
    sys.exit(0)


nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
total = dias * preco_diaria

print(
    f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto}"
    f"O valor total estimado será R$ {total:.2f}"

)

if input("Confirma (digite y)").strip().lower() in ("y", "yes","sim", "s"):
   with open(RESERVAS_FILE, "a") as reserva_file:
      reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")



