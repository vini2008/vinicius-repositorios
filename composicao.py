"""imprimir todos os nomes que começem com B"""


names = [
   "Bruno",
   "Joao",
   "Bernado",
   "Barbara", 
   "Brian",
]
print("#" * 16)
print("Estilo funcional")
print(*list(filter(lambda text: text[0].lower() == "b" ,names)), sep="\n")
print("" * 40)
print("#" * 17)

print("Estilo procedural")


def start_with_b(text):
    return text[0].lower() == "b"


filtro = filter(start_with_b ,names)
filtro = list(filtro)

for name in filtro:
    print(name)
print("" * 40)
